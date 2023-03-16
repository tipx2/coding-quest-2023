import requests
from collections import deque

lines = requests.get("https://codingquest.io/api/puzzledata?puzzle=26").text.split("\n")


class Node:
    def __init__(self, val):
        self.l = None
        self.r = None
        self.v = val

class BinaryTree:

    def __init__(self):
        self.root = None

    def add(self, val):
        if self.root is None:
            self.root = Node(val)
        else:
            self._add(val, self.root)

    def _add(self, val, node):
        if val < node.v:
            if node.l is not None:
                self._add(val, node.l)
            else:
                node.l = Node(val)
        else:
            if node.r is not None:
                self._add(val, node.r)
            else:
                node.r = Node(val)
    
    def find_depth(self, node):
        if node.l == None and node.r == None:
            return 1
        if node.l == None:
            return 1 + self.find_depth(node.r)
        elif node.r == None:
            return 1 + self.find_depth(node.l)
        return 1 + max(self.find_depth(node.l), self.find_depth(node.r))
    
    def max_width(self):
        if self.root is None:
            return 0

        q = deque([self.root])
        max_width = 1

        while len(q) > 0:
            level_width = len(q)
            max_width = max(max_width, level_width)

            for _ in range(level_width):
                node = q.popleft()

                if node.l is not None:
                    q.append(node.l)
                if node.r is not None:
                    q.append(node.r)

        return max_width



tree = BinaryTree()
for line in lines:
    val = int(line, 16)
    tree.add(val)

print(tree.find_depth(tree.root) * tree.max_width())
print()
