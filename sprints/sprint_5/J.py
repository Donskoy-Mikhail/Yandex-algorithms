import sys
import os

sys.setrecursionlimit(3000)


LOCAL = os.environ.get('REMOTE_JUDGE', 'false') != 'true'

if not LOCAL:
    from node import Node

if LOCAL:
    class Node:
        def __init__(self, left=None, right=None, value=0):
            self.right = right
            self.left = left
            self.value = value


def insert(root, key) -> Node:
    if root is not None:
        if root.value > key:
            if root.left is not None:
                insert(root.left, key)
            else:
                root.left = Node(value=key)
        else:
            if root.right is not None:
                insert(root.right, key)
            else:
                root.right = Node(value=key)
    else:
        root = Node(value=key)
    return root

def test():
    node1 = Node(None, None, 7)
    node2 = Node(node1, None, 8)
    node3 = Node(None, node2, 7)
    new_head = insert(node3, 6)
    assert new_head is node3
    assert new_head.left.value == 6


if __name__ == '__main__':
    test()