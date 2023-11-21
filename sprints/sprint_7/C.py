import sys


if __name__ == "__main__":
    m = int(sys.stdin.readline().rstrip())
    n = int(sys.stdin.readline().rstrip())
    profit = 0
    heaps = []

    for _ in range(n):
        heaps.append([*map(int, input().split())])

    heaps.sort(key=lambda x: x[0], reverse=True)

    for heap in heaps:
        if m == 0:
            break
        elif heap[1] >= m:
            profit += m * heap[0]
            m = m - m
        elif heap[1] < m:
            profit += heap[1] * heap[0]
            m = m - heap[1]
    print(profit)
