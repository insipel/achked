"""
LeetCode 2296. Design a Text Editor
https://leetcode.com/problems/design-a-text-editor/

Design a text editor with a cursor that can:
  - Add text to where the cursor is.
  - Delete text from where the cursor is (like backspace).
  - Move the cursor left or right.

Approach: two stacks.
  `left`  holds the characters to the LEFT of the cursor, in order,
          with the character closest to the cursor on top (end of list).
  `right` holds the characters to the RIGHT of the cursor, in order,
          with the character closest to the cursor on top (end of list).

The cursor conceptually sits between `left` and `right`. Every operation
only touches the ends of these two lists, so each call is O(1) amortized
(list.append / list.pop at the end of a Python list are O(1)).

  addText(text):      push each char of `text` onto `left`.
  deleteText(k):      pop up to k chars off `left`; return how many were
                       actually removed.
  cursorLeft(k):      move up to k chars from the top of `left` to the
                       top of `right` (shifting the cursor left), then
                       report the last min(10, len(left)) chars of `left`.
  cursorRight(k):     move up to k chars from the top of `right` to the
                       top of `left` (shifting the cursor right), then
                       report the last min(10, len(left)) chars of `left`.

Total work across all calls is bounded by the total number of characters
ever moved between the two stacks, which is linear in the sum of the
input sizes -- well within LeetCode's limits (up to 2*10^4 calls).
"""

from typing import List


class TextEditor:
    def __init__(self):
        self.left: List[str] = []   # chars before the cursor, nearest-to-cursor last
        self.right: List[str] = []  # chars after the cursor, nearest-to-cursor last

    def addText(self, text: str) -> None:
        self.left.extend(text)

    def deleteText(self, k: int) -> int:
        removed = min(k, len(self.left))
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


if __name__ == "__main__":
    # Sanity check against the example from the problem statement:
    #
    # ["TextEditor", "addText", "deleteText", "addText", "cursorRight",
    #  "cursorLeft", "deleteText", "cursorLeft", "cursorRight"]
    # [[], ["leetcode"], [4], ["practice"], [3], [8], [10], [2], [6]]
    #
    # Output:
    # [null, null, 4, null, "etpractice", "leet", 4, "", "practi"]
    ops = ["TextEditor", "addText", "deleteText", "addText", "cursorRight",
           "cursorLeft", "deleteText", "cursorLeft", "cursorRight"]
    args = [[], ["leetcode"], [4], ["practice"], [3],
            [8], [10], [2], [6]]
    expected = [None, None, 4, None, "etpractice", "leet", 4, "", "practi"]

    editor = None
    results = []
    for op, arg in zip(ops, args):
        if op == "TextEditor":
            editor = TextEditor()
            results.append(None)
        else:
            results.append(getattr(editor, op)(*arg))

    print("got:     ", results)
    print("expected:", expected)
    assert results == expected, "Mismatch against official example!"
    print("Example passed.")
