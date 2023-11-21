import sys
from decimal import Decimal

if __name__ == "__main__":
    n = int(input())
    times = []
    for _ in range(n):
        times.append((*map(Decimal, sys.stdin.readline().rstrip().split()),))
    times.sort(key=lambda x: (x[1], -(x[1] - x[0])))
    result = []
    cur_time = None
    for el in times:
        if cur_time is None or el[0] >= cur_time:
            result.append(el)
            cur_time = el[1]
    print(len(result))
    for time in result:
        print(str(time[0]), str(time[1]))