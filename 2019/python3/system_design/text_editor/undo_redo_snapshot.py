"""
Text Editor with Undo/Redo -- snapshot approach.

Builds on the two-stack TextEditor from LeetCode 2296 (Design a Text
Editor): `left` holds characters before the cursor, `right` holds
characters after the cursor, cursor-adjacent character on top of each.

Undo/redo strategy: before every content-changing operation (addText /
deleteText), push a *copy* of both `left` and `right` onto `undo_stack`.
`.copy()` matters -- storing the same list objects would just give you
two references to state that keeps mutating, not an actual snapshot in
time. `undo()` swaps the current (left, right) out for the top of
undo_stack (after first saving the current state onto redo_stack so redo
can restore it); `redo()` does the mirror image.

Cursor moves (cursorLeft / cursorRight) are NOT snapshotted, matching how
most editors behave: undo reverts edits, not cursor navigation. Because
`left`/`right` already encode cursor position, undoing an edit naturally
restores the cursor to wherever it was at the time of that edit.

Complexity: each snapshot is O(length of the line) because `.copy()`
walks the whole list, so addText/deleteText/undo/redo are all O(n)
instead of the base structure's O(1) amortized. For a one-line editor
(bounded, typically short buffer) this overhead is negligible in
practice, and in exchange there is no per-operation-type inverse logic to
get wrong -- undo/redo are just "restore the exact prior state," which is
correct by construction no matter what operations get added later.
"""

from typing import List, Tuple


class TextEditor:
    def __init__(self):
        self.left: List[str] = []   # chars before the cursor, nearest-to-cursor last
        self.right: List[str] = []  # chars after the cursor, nearest-to-cursor last
        self.undo_stack: List[Tuple[List[str], List[str]]] = []
        self.redo_stack: List[Tuple[List[str], List[str]]] = []

    def _snapshot_current(self) -> Tuple[List[str], List[str]]:
        return (self.left.copy(), self.right.copy())

    def _push_undo_snapshot(self) -> None:
        self.undo_stack.append(self._snapshot_current())
        self.redo_stack.clear()  # a fresh edit invalidates the old redo branch

    # ---- public LeetCode-style API ----

    def addText(self, text: str) -> None:
        if not text:
            return
        self._push_undo_snapshot()
        self.left.extend(text)

    def deleteText(self, k: int) -> int:
        removed = min(k, len(self.left))
        if removed == 0:
            return 0
        self._push_undo_snapshot()
        del self.left[len(self.left) - removed:]
        return removed

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
        self.redo_stack.append(self._snapshot_current())
        self.left, self.right = self.undo_stack.pop()

    def redo(self) -> None:
        if not self.redo_stack:
            return
        self.undo_stack.append(self._snapshot_current())
        self.left, self.right = self.redo_stack.pop()

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

    # Undo/redo walkthrough -- identical scenario to the command-log file,
    # so the two implementations can be checked against each other.
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

    print("Undo/redo (snapshot) checks passed.")
