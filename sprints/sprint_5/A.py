# ! change LOCAL to False before submitting !
# set LOCAL to True for local testing
import os

LOCAL = os.environ.get('REMOTE_JUDGE', 'false') != 'true'

if LOCAL:
    class Node:
        def __init__(self, value, left=None, right=None):
            self.value = value
            self.right = right
            self.left = left


def solution(root) -> int:
    if root is not None:

        if root.right:
            val_r = solution(root.right)
            max_val = max(max_val, val_r)

        if root.left:
            val_l = solution(root.left)
            max_val = max(max_val, val_l)
        return max_val


def test():
    node1 = Node(1)
    node2 = Node(-5)
    node3 = Node(3, node1, node2)
    node4 = Node(2, node3, None)
    assert solution(node4) == 3


if __name__ == '__main__':
    test()