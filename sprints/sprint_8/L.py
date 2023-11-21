import sys


def prefix_func(s):
    pi = [-1 for _ in range(len(s))]
    pi[0] = 0

    for i in range(1, len(s)):
        k = pi[i - 1]
        while k > 0 and s[k] != s[i]:
            k = pi[k - 1]
        if s[k] == s[i]:
            k += 1

        pi[i] = k

    return pi


if __name__ == '__main__':
    print(' '.join(map(str, prefix_func(sys.stdin.readline().rstrip()))))
