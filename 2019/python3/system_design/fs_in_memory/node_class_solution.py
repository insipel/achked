"""
LeetCode 588. Design In-Memory File System

Implementation using an explicit Node class rather than raw nested
dicts. Each Node represents either a directory or a file:

- A directory node has `children`, a dict mapping child name -> Node,
  and `is_file = False`.
- A file node has `is_file = True` and holds its data in `content`.

This is the same k-ary tree shape as the nested-dict version, but
file vs. directory is tracked explicitly via `is_file` instead of
relying on Python's dynamic typing (isinstance checks). That makes it
port cleanly to statically typed languages, and gives each node a
natural place to hang extra metadata later (timestamps, permissions,
size, etc.) if a follow-up ever asks for it.
"""


class Node:
    def __init__(self):
        self.children = {}   # name -> Node
        self.is_file = False
        self.content = ""


class FileSystem:
    def __init__(self):
        self.root = Node()

    def _walk(self, path):
        node = self.root
        if path == "/":
            return node
        for part in path.split("/")[1:]:
            node = node.children[part]
        return node

    def mkdir(self, path):
        node = self.root
        for part in path.split("/")[1:]:
            if part not in node.children:
                node.children[part] = Node()
            node = node.children[part]

    def addContentToFile(self, filePath, content):
        parts = filePath.split("/")[1:]
        node = self.root
        for part in parts[:-1]:
            if part not in node.children:
                node.children[part] = Node()
            node = node.children[part]

        name = parts[-1]
        if name not in node.children:
            node.children[name] = Node()
        file_node = node.children[name]
        file_node.is_file = True
        file_node.content += content

    def readContentFromFile(self, filePath):
        node = self._walk(filePath)
        return node.content

    def ls(self, path):
        node = self._walk(path)
        if node.is_file:
            return [path.split("/")[-1]]
        return sorted(node.children.keys())


if __name__ == "__main__":
    fs = FileSystem()
    print(fs.ls("/"))                              # []
    fs.mkdir("/a/b/c")
    fs.addContentToFile("/a/b/c/d", "hello")
    print(fs.ls("/"))                              # ["a"]
    print(fs.readContentFromFile("/a/b/c/d"))       # "hello"
