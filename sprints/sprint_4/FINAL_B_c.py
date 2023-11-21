class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashTable:
    def __init__(self, size=10 ** 5):
        self._size = size
        self._table = [None] * size

    def _hash(self, key):
        return key % self._size

    def put(self, key, value):
        hash_value = self._hash(key)

        if self._table[hash_value] is None:
            self._table[hash_value] = Node(key, value)
        else:
            current = self._table[hash_value]
            if current.key == key:
                current.value = value
                return None
            while current.next is not None:
                if current.key == key:
                    current.value = value
                    return None
                current = current.next
            current.next = Node(key, value)

    def get(self, key):
        hash_value = self._hash(key)
        current = self._table[hash_value]
        if current is None:
            return None
        while current is not None:
            if current.key == key:
                return current.value
            current = current.next

        return None

    def delete(self, key):
        hash_value = self._hash(key)
        current = self._table[hash_value]
        prev = None
        if current is None:
            return None
        while current is not None:
            if current.key == key:
                value = current.value
                if prev is None:
                    self._table[hash_value] = current.next
                else:
                    prev.next = current.next
                return value
            prev = current
            current = current.next

        return None


if __name__ == "__main__":
    n = int(input())

    hash_table = HashTable()

    for _ in range(n):
        command = input().split()
        operation = command[0]
        if operation == "get":
            print(hash_table.get(int(command[1])))
        elif operation == "put":
            hash_table.put(int(command[1]), int(command[2]))
        else:
            print(hash_table.delete(int(command[1])))
