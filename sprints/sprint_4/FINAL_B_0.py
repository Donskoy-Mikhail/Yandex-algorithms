class HashTable:
    def __init__(self, size=109859):
        self._size = size
        self._table = [None] * size
        self._c = 3

    def _hash(self, key):
        return key % self._size

    def put(self, key, value):
        hash_value = self._hash(key)
        if self._table[hash_value] is None:
            self._table[hash_value] = (key, value)
        else:
            while self._table[hash_value] is not None:
                if self._table[hash_value][0] == key:
                    break
                hash_value = (hash_value + 2 * self._c) % self._size
            self._table[hash_value] = (key, value)

    def get(self, key):
        hash_value = self._hash(key)
        if self._table[hash_value] is None:
            return None
        else:
            while self._table[hash_value] is not None:
                if self._table[hash_value][0] == key:
                    return self._table[hash_value][1]
                hash_value = (hash_value + 2 * self._c) % self._size

    def delete(self, key):
        hash_value = self._hash(key)
        if self._table[hash_value] is None:
            return None
        else:
            while self._table[hash_value] is not None:
                if self._table[hash_value][0] == key:
                    value = self._table[hash_value][1]
                    self._table[hash_value] = None
                    return value
                hash_value = (hash_value + 2 * self._c) % self._size


if __name__ == "__main__":
    n = int(input())

    hash_table = HashTable()

    for _ in range(n):
        command = input().split()
        operation = command[0]
        if operation == "put":
            hash_table.put(int(command[1]), int(command[2]))
        elif operation == "get":
            print(hash_table.get(int(command[1])))
        else:
            print(hash_table.delete(int(command[1])))

