import sys


if __name__ == "__main__":
    s = sys.stdin.readline().rstrip()
    n = int(sys.stdin.readline().rstrip())

    to_insert = {}

    for _ in range(n):
        t, k = sys.stdin.readline().rstrip().split()
        k = int(k)

        to_insert[k] = t

    res = []

    for n, s_i in enumerate(s):
        if n == 0:
            res.append(to_insert.get(0, '') + s_i + to_insert.get(1, ''))
        else:
            res.append(s_i + to_insert.get(n + 1, ''))

    print(''.join(res))
