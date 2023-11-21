import sys
class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

a = None
b = Node(10, 13)
c = [None for _ in range(14) ]

print(sys.getsizeof(a))
print(sys.getsizeof(b))
print(sys.getsizeof(c))