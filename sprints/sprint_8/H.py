def find(p, text):
    result = []
    s = p + '#' + text
    pi = [0 for _ in range(len(p))]

    pi_prev = 0

    for i in range(1, len(s)):
        k = pi_prev
        while (k > 0) and (s[k] != s[i]):
            k = pi[k - 1]
        if s[k] == s[i]:
            k += 1

        if i < len(p):
            pi[i] = k

        pi_prev = k

        if k == len(p):
            result.append((i - 2 * len(p)))

    return result


import sys


def replace(text, old, new):
    s = old + '#' + text
    pi = [0 for _ in range(len(old))]
    pi_prev = 0
    result = []

    for i in range(1, len(s)):
        k = pi_prev
        while (k > 0) and (s[k] != s[i]):
            k = pi[k - 1]
        if s[k] == s[i]:
            k += 1
        if i < len(old):
            pi[i] = k

        if i > len(old):
            result.append(s[i])

        pi_prev = k

        if k == len(old):
            for _ in range(len(old)):
                result.pop()

            for new_s in new:
                result.append(new_s)

    return ''.join(result)


def main():
    a = sys.stdin.readline().rstrip()
    s = sys.stdin.readline().rstrip()
    t = sys.stdin.readline().rstrip()

    print(replace(a, s, t))


if __name__ == '__main__':
    main()
