"""
LeetCode 588. Design In-Memory File System

Implementation using a "hashmap of hashmaps" approach instead of an
explicit Node class. Each directory is represented by a plain dict
mapping child name -> child (another dict for a subdirectory, or a
string for a file's content). The two are told apart at read time via
isinstance(), since Python dicts/strs are dynamically typed.

Trade-off vs. a Node-class tree:
- Pros: less boilerplate, natural recursive structure.
- Cons: relies on dynamic typing to distinguish file vs. directory
  (doesn't port cleanly to statically typed languages), and there's
  nowhere natural to hang extra metadata (timestamps, permissions,
  size) on a file without wrapping it in something richer.
"""


class FileSystem:
    def __init__(self):
        self.root = {}

    def _walk(self, path):
        node = self.root
        if path == "/":
            return node
        for part in path.split("/")[1:]:
            node = node[part]
        return node

    def mkdir(self, path):
        node = self.root
        for part in path.split("/")[1:]:
            node = node.setdefault(part, {})

    def addContentToFile(self, filePath, content):
        parts = filePath.split("/")[1:]
        node = self.root
        for part in parts[:-1]:
            node = node.setdefault(part, {})
        node[parts[-1]] = node.get(parts[-1], "") + content

    def readContentFromFile(self, filePath):
        parts = filePath.split("/")[1:]
        node = self.root
        for part in parts[:-1]:
            node = node[part]
        return node[parts[-1]]

    def ls(self, path):
        node = self._walk(path)
        if isinstance(node, str):
            return [path.split("/")[-1]]
        return sorted(node.keys())


if __name__ == "__main__":
    fs = FileSystem()
    print(fs.ls("/"))                              # []
    fs.mkdir("/a/b/c")
    fs.addContentToFile("/a/b/c/d", "hello")
    print(fs.ls("/"))                              # ["a"]
    print(fs.readContentFromFile("/a/b/c/d"))       # "hello"
