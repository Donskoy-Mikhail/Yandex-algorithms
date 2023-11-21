"""
89992782

-- ПРИНЦИП РАБОТЫ --

Алгоритм спускается вниз по дереву до тех пор пока не на найдет
вершину с искомым значеним после чего заменяет искомую вершину своей
существующей дочерней вершиной (если одна из вершин не существует)
или если существуют обе дочерние вершины то ищет самую маленькую вершину в
правой дочерней вершине, заменяет на нее искомую для удаления
и после удаляет найденную минимальную вершину в правом поддереве
рекурсивным вызовом самой себя remove

 -- ДОКАЗАТЕЛЬСТВО КОРРЕКТНОСТИ --

Алгоритм работает за счет того что он рекурсивно спускается вниз
за счет вызова самого себя над вершиной где может находится искомая
вершина и если ни одно из условий проверки вершины не выполнено <>=,
то сама функция возвращает корень который ей передался, что позволяет
как удалить искомую вершину и заменить ее на другую, так и просто не изменять
деревево когда дошли до конца и не нашли искомое значение

Допустим мы нашли вершину с искомомым значением, если у нее
отсутвует один из предков то мы заменим ее другой существующей вершиной

Допустим мы нашли вершину с искомомым значением, если у нее
отсутвуют оба предка то мы просто заменим ее на None

    if root.left is None:
        return root.right
    elif root.right is None:
        return root.left

В таком случае вернет None

Допустим мы нашли вершину с искомомым значением, если у нее
есть оба предка то м ищем самую левую вершину в правом поддереве

min_right = root.right
while min_right.left is not None:
    min_right = min_right.left

Заменяем в удаляемой вершине значение на найденное min_right.value
и далее вызываем над удаляемой вершиной рекурсивно  remove(min_right, min_right.value)
что позволяет нам удалить вершину на которую мы заменили удаленную искомую вершину

-- ВРЕМЕННАЯ СЛОЖНОСТЬ --

В худшем случае сложность O(N) где n количество узлов в дереве
В среднем сложность будет стремиться к O(log n) поскольку в среднем деревья должны
быть больше похожи на сбалансированные нежели чем на  ццепочку узлов


-- ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ --

История аналогичная тому как и во временной сложности, чем глубже рекурсия тем больше требуется доп
памяти:

В худшем случае сложность O(N) где n количество узлов в дереве
В среднем сложность будет стремиться к O(log n) поскольку в среднем деревья должны
быть больше похожи на сбалансированные нежели чем на  ццепочку узлов

"""

from typing import Optional
import os

LOCAL = os.environ.get('REMOTE_JUDGE', 'false') != 'true'

if LOCAL:
    class Node:
        def __init__(self, left=None, right=None, value=0):
            self.right = right
            self.left = left
            self.value = value
else:
    from node import Node


def remove(root, key):
    if root is None:
        return root

    if key < root.value:
        root.left = remove(root.left, key)
    elif key > root.value:
        root.right = remove(root.right, key)
    else:
        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left

        min_right = root.right
        while min_right.left is not None:
            min_right = min_right.left

        root.value = min_right.value

        root.right = remove(root.right, min_right.value)

    return root


def test():
    node1 = Node(None, None, 2)
    node2 = Node(node1, None, 3)
    node3 = Node(None, node2, 1)
    node4 = Node(None, None, 6)
    node5 = Node(node4, None, 8)
    node6 = Node(node5, None, 10)
    node7 = Node(node3, node6, 5)
    newHead = remove(node7, 10)
    assert newHead.value == 5
    assert newHead.right is node5
    assert newHead.right.value == 8


if __name__ == '__main__':
    test()