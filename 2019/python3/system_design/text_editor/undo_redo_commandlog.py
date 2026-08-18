"""
Text Editor with Undo/Redo -- command-log approach.

Builds on the two-stack TextEditor from LeetCode 2296 (Design a Text
Editor): `left` holds characters before the cursor, `right` holds
characters after the cursor, cursor-adjacent character on top of each.

Undo/redo strategy: instead of snapshotting the whole buffer, we log just
the *content-changing* operations (addText / deleteText) with enough
information to reverse them -- for addText, the text that was added; for
deleteText, the text that was actually removed (not just the count `k`,
since fewer than `k` characters may have been available). Cursor moves
(cursorLeft / cursorRight) are NOT logged as separate undo steps, matching
how most editors behave: undo reverts edits, not cursor navigation.

Both addText's inverse and deleteText's inverse turn out to be the *other*
operation applied to the *same text*:
    inverse of "added text T"   -> delete len(T) chars
    inverse of "deleted text T" -> re-add T

IMPORTANT correctness subtlety #1: it's not enough to just replay the
inverse at the *current* cursor position. If the cursor moved (via
cursorLeft / cursorRight) after an edit and before that edit is undone,
the edited text may no longer sit at the end of `left` -- part of it can
now be in `right`. So each logged command also records the buffer
position (cursor index) the edit was applied at; undo/redo first
reposition the cursor back to the right spot (shuffling between
`left`/`right`, the same primitive cursorLeft/cursorRight use) before
replaying the inverse or the original op. An earlier version of this file
skipped that repositioning step and silently corrupted the buffer
whenever a cursor move happened between an edit and its undo -- caught by
cross-checking against the snapshot implementation with randomized
operation sequences.

IMPORTANT correctness subtlety #2: where should the cursor land after a
redo (or a second undo of the same edit), if the cursor was moved
independently at some point in between? The only answer that stays
consistent under *arbitrary* interleavings of edits, undos, redos, and
cursor moves is fully symmetric: every time an entry is pushed onto
either stack -- whether by a fresh addText/deleteText, or by undo()
un-applying it, or by redo() re-applying it -- record wherever the cursor
happened to be right before that push. The next time this same entry is
popped off (from the opposite stack), land there, in addition to the
position that's structurally forced by the edit's own content boundary.
This is exactly what the snapshot approach gets "for free": swapping raw
(left, right) state is unconditionally correct for any interleaving,
because it never tries to reconstruct position from first principles. The
command-log approach has to earn the same guarantee by explicitly
threading a "resume position" through every push/pop -- get only the
undo->redo half of that right (as an earlier version of this file did)
and it still corrupts content on some later edit, because a subsequent
redo/undo pair lands the cursor somewhere the snapshot version wouldn't,
and every add/delete after that operates at a different logical position.
Caught by cross-checking hundreds of randomized operation sequences
against the snapshot implementation and asserting full state equality,
not just equal visible text.

Complexity: addText/deleteText stay O(1) amortized, same as the base
structure -- no per-edit buffer copy. undo/redo are O(distance the cursor
must move to reach the edit's position), which is at most O(n) but often
much less. That's the real advantage over the snapshot approach: snapshot
pays an O(n) copy on *every single edit* whether or not undo is ever
used, whereas here the extra cost only shows up on the undo/redo calls
themselves.
"""

from typing import List, Tuple

# (op, text, position_before, target_position)
#   op:               "add" or "delete"
#   text:             the literal text added, or the text actually removed
#   position_before:  cursor index (len(left)) when this edit was FIRST applied --
#                      fixed forever, defines the edit's content boundary
#   target_position:  cursor index to land on, captured right before whichever
#                      call (add/delete/undo/redo) most recently pushed this
#                      entry onto its current stack
HistoryEntry = Tuple[str, str, int, int]


class TextEditor:
    def __init__(self):
        self.left: List[str] = []   # chars before the cursor, nearest-to-cursor last
        self.right: List[str] = []  # chars after the cursor, nearest-to-cursor last
        self.undo_stack: List[HistoryEntry] = []
        self.redo_stack: List[HistoryEntry] = []

    # ---- low-level buffer mutation (no history bookkeeping) ----

    def _apply_add(self, text: str) -> None:
        self.left.extend(text)

    def _apply_delete(self, k: int) -> str:
        """Remove up to k chars from the end of `left`; return what was removed."""
        removed_count = min(k, len(self.left))
        if removed_count == 0:
            return ""
        removed = "".join(self.left[len(self.left) - removed_count:])
        del self.left[len(self.left) - removed_count:]
        return removed

    def _move_cursor_to(self, position: int) -> None:
        """Reposition the left/right split to an absolute buffer index."""
        while len(self.left) > position:
            self.right.append(self.left.pop())
        while len(self.left) < position:
            self.left.append(self.right.pop())

    # ---- public LeetCode-style API ----

    def addText(self, text: str) -> None:
        if not text:
            return
        position_before = len(self.left)
        self._apply_add(text)
        # Fresh entry: nothing to "resume" yet, so target == position_before.
        self.undo_stack.append(("add", text, position_before, position_before))
        self.redo_stack.clear()  # a fresh edit invalidates the old redo branch

    def deleteText(self, k: int) -> int:
        position_before = len(self.left)
        removed = self._apply_delete(k)
        if removed:
            self.undo_stack.append(("delete", removed, position_before, position_before))
            self.redo_stack.clear()
        return len(removed)

    def cursorLeft(self, k: int) -> str:
        move = min(k, len(self.left))
        for _ in range(move):
            self.right.append(self.left.pop())
        return self._last_ten()

    def cursorRight(self, k: int) -> str:
        move = min(k, len(self.right))
        for _ in range(move):
            self.left.append(self.right.pop())
        return self._last_ten()

    def _last_ten(self) -> str:
        return "".join(self.left[max(0, len(self.left) - 10):])

    # ---- undo / redo ----

    def undo(self) -> None:
        if not self.undo_stack:
            return
        op, text, position_before, target_position = self.undo_stack.pop()
        # Wherever the cursor is right now becomes the spot a future redo
        # should return to -- captured BEFORE we touch anything below.
        position_now = len(self.left)
        if op == "add":
            # Text sits at [position_before, position_before + len(text)).
            # Move the cursor to the end of it, then delete it off the back.
            self._move_cursor_to(position_before + len(text))
            self._apply_delete(len(text))
        else:  # op == "delete"
            # Text used to sit right before position_before; the buffer is
            # currently split at position_before - len(text). Move there
            # and re-add it.
            self._move_cursor_to(position_before - len(text))
            self._apply_add(text)
        # Structural reversal necessarily lands exactly on position_before;
        # now additionally honor this entry's own resume target (relevant
        # if it had previously been redone with cursor drift in between).
        self._move_cursor_to(target_position)
        self.redo_stack.append((op, text, position_before, position_now))

    def redo(self) -> None:
        if not self.redo_stack:
            return
        op, text, position_before, target_position = self.redo_stack.pop()
        # Symmetric to undo(): remember where we are before mutating, for
        # a possible future undo of this same entry to return to.
        position_now = len(self.left)
        # Both add and delete were originally applied at position_before --
        # reposition there so the content lands in exactly the same place.
        self._move_cursor_to(position_before)
        if op == "add":
            self._apply_add(text)
        else:  # op == "delete"
            self._apply_delete(len(text))
        # Structural reapplication lands naturally right after/before the
        # text; now additionally honor this entry's resume target.
        self._move_cursor_to(target_position)
        self.undo_stack.append((op, text, position_before, position_now))

    # ---- convenience (not part of the LeetCode spec, useful for testing) ----

    def getText(self) -> str:
        """Full current line, left-to-right, cursor position not shown."""
        return "".join(self.left) + "".join(reversed(self.right))


if __name__ == "__main__":
    # Original LeetCode example still passes -- undo/redo bookkeeping
    # doesn't change the base behavior.
    ops = ["TextEditor", "addText", "deleteText", "addText", "cursorRight",
           "cursorLeft", "deleteText", "cursorLeft", "cursorRight"]
    args = [[], ["leetcode"], [4], ["practice"], [3], [8], [10], [2], [6]]
    expected = [None, None, 4, None, "etpractice", "leet", 4, "", "practi"]

    editor = None
    results = []
    for op, arg in zip(ops, args):
        if op == "TextEditor":
            editor = TextEditor()
            results.append(None)
        else:
            results.append(getattr(editor, op)(*arg))
    assert results == expected, f"LeetCode example mismatch: {results}"
    print("LeetCode example passed.")

    # Undo/redo walkthrough.
    e = TextEditor()
    e.addText("hello")
    assert e.getText() == "hello"
    e.addText(" world")
    assert e.getText() == "hello world"

    e.undo()
    assert e.getText() == "hello", e.getText()
    e.undo()
    assert e.getText() == "", e.getText()

    e.redo()
    assert e.getText() == "hello", e.getText()

    removed = e.deleteText(3)  # removes "llo"
    assert removed == 3 and e.getText() == "he", e.getText()

    e.undo()  # reinsert "llo"
    assert e.getText() == "hello", e.getText()

    # A brand-new edit after an undo should discard the old redo branch.
    e.addText("!!!")
    assert e.getText() == "hello!!!", e.getText()
    e.redo()  # nothing to redo -- redo_stack was cleared by addText above
    assert e.getText() == "hello!!!", e.getText()

    # undo/redo on an empty stack are no-ops, not errors.
    empty = TextEditor()
    empty.undo()
    empty.redo()
    assert empty.getText() == ""

    # Regression: cursor moving between an edit and its undo must not
    # corrupt the buffer -- the edited text can end up split across
    # left/right by the time undo() runs.
    e2 = TextEditor()
    e2.addText("hello")
    e2.cursorLeft(2)            # text is "hel|lo", cursor before "lo"
    e2.undo()                   # should fully remove "hello", not just "hel"
    assert e2.getText() == "", e2.getText()

    # Regression: cursor drift *before* an undo must be preserved through
    # a later redo (undo->redo direction).
    e3 = TextEditor()
    e3.addText("ab")            # left=['a','b']
    e3.cursorLeft(1)            # left=['a'], right=['b'] -- cursor drifts to 1
    e3.undo()                   # removes "ab" entirely
    e3.redo()                   # should land back at the drifted position 1,
    assert (e3.left, e3.right) == (['a'], ['b']), (e3.left, e3.right)

    # Regression: cursor drift *after* an undo (i.e. between undo and a
    # later redo) must also be preserved through a *second* undo
    # (redo->undo direction) -- this is the direction an earlier fix missed.
    e4 = TextEditor()
    e4.addText("wcsbt")
    e4.deleteText(8)            # removes all of "wcsbt"
    e4.undo()                   # reinstates "wcsbt", cursor at end (position 5)
    e4.cursorLeft(5)            # cursor drifts to position 0
    e4.redo()                   # re-deletes "wcsbt"; lands back at position 0
    e4.undo()                   # should land back at position 0 again, not 5
    assert (e4.left, e4.right) == ([], list("tbscw")), (e4.left, e4.right)

    print("Undo/redo (command-log) checks passed.")
