class HashTable:
    def __init__(self, size=109859):
        self.size = size
        self.table = [[] for _ in range(size)]

    def _hash(self, key):
        return key % self.size

    def put(self, key, value):
        hash_value = self._hash(key)
        for item in self.table[hash_value]:
            if item[0] == key:
                item[1] = value
                return None
        self.table[hash_value].append([key, value])

    def get(self, key):
        hash_value = self._hash(key)
        for item in self.table[hash_value]:
            if item[0] == key:
                return item[1]
        return None

    def delete(self, key):
        hash_value = self._hash(key)
        for idx, item in enumerate(self.table[hash_value]):
            if item[0] == key:
                value = item[1]
                del self.table[hash_value][idx]
                return value
        return None


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