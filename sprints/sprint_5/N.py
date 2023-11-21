import os

LOCAL = os.environ.get('REMOTE_JUDGE', 'false') != 'true'

if LOCAL:
    class Node:
        def __init__(self, left=None, right=None, value=0, size=0):
            self.right = right
            self.left = left
            self.value = value
            self.size = size


def split(root, k):
    if not root:
        return None, None

    if k <= 0:
        return None, root

    # Размер поддерева слева
    left_size = root.left.size if root.left else 0

    if k > left_size + 1:
        # Если k больше размера поддерева слева (включая текущую вершину), рекурсивно вызываем функцию для правого поддерева
        left, right = split(root.right, k - left_size - 1)
        root.right = left
        # Пересчитываем размер текущей вершины
        root.size = left_size + 1 + (left.size if left else 0)
        return root, right
    else:
        # Если k меньше или равно размеру поддерева слева (включая текущую вершину), рекурсивно вызываем функцию для левого поддерева
        left, right = split(root.left, k)
        root.left = right
        # Пересчитываем размер текущей вершины
        root.size = left_size + 1 + (right.size if right else 0)
        return left, root


def test():
    node1 = Node(None, None, 3, 1)
    node2 = Node(None, node1, 2, 2)
    node3 = Node(None, None, 8, 1)
    node4 = Node(None, None, 11, 1)
    node5 = Node(node3, node4, 10, 3)
    node6 = Node(node2, node5, 5, 6)
    left, right = split(node6, 4)
    assert (left.size == 4)
    assert (right.size == 2)


if __name__ == '__main__':
    test()