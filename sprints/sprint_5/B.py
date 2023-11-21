import os
import sys

LOCAL = os.environ.get('REMOTE_JUDGE', 'false') != 'true'

sys.setrecursionlimit(3000)

if LOCAL:
    class Node:
        def __init__(self, value, left=None, right=None):
            self.value = value
            self.right = right
            self.left = left


def solution(root) -> bool:
    def height(root):
        if root is None:
            return 0
        hr = height(root.right)
        hl = height(root.left)

        return max(hr, hl) + 1

    if root is None:
        return True

    hr = height(root.right)
    hl = height(root.left)
    if abs(hr - hl) > 1:
        return False

    return solution(root.left) and solution(root.right)

def test():
    node1 = Node(1)
    node2 = Node(-5)
    node3 = Node(3, node1, node2)
    node4 = Node(10)
    node5 = Node(2, node3, node4)
    assert solution(node5)


if __name__ == '__main__':
    test()