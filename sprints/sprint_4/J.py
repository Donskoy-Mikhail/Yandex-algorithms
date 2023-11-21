def find_quadruples(arr, target):
    n = len(arr)
    hash_table = {}
    quadruples = set()

    for i in range(n - 1):
        for j in range(i + 1, n):
            current_sum = arr[i] + arr[j]
            if target - current_sum in hash_table:
                for indexes in hash_table[target - current_sum]:
                    if i not in indexes and j not in indexes:
                        quadruples.add(tuple(sorted([arr[i], arr[j], arr[indexes[0]], arr[indexes[1]]])))
            if current_sum not in hash_table:
                hash_table[current_sum] = []
            hash_table[current_sum].append((i, j))

    return sorted(list(quadruples))


if __name__ == "__main__":

    n = int(input())
    target = int(input())
    arr = list(map(int, input().split()))

    quadruples = find_quadruples(arr, target)
    print(len(quadruples))
    for quad in quadruples:
        print(*quad)
