import sys


def search(n, x, m, a):
    a_diff = []

    for n in range(len(a) - 1):
        a_diff.append(a[n + 1] - a[n])

    res = []

    for n in range(len(x) - len(a) + 1):
        match = True
        for offset in range(len(a) - 1):
            if x[n + offset + 1] - x[n + offset] != a_diff[offset]:
                match = False
                break

        if match:
            res.append(n)
    return ' '.join(map(str, map(lambda e: e + 1, res)))


if __name__ == "__main__":
    n = int(sys.stdin.readline().rstrip())
    x = list(map(int, sys.stdin.readline().rstrip().split()))
    m = int(sys.stdin.readline().rstrip())
    a = list(map(int, sys.stdin.readline().rstrip().split()))

    print(search(n, x, m, a))
