import sys
import string


if __name__ == '__main__':
    a = sys.stdin.readline().rstrip()
    b = sys.stdin.readline().rstrip()

    valid_symbols = []

    for n, s in enumerate(string.ascii_lowercase):
        if (n + 1) % 2 == 0:
            valid_symbols.append(s)

    a_f = ''.join(filter(lambda e: e in valid_symbols, a))
    b_f = ''.join(filter(lambda e: e in valid_symbols, b))

    if a_f == b_f:
        print(0)
    elif a_f > b_f:
        print(1)
    else:
        print(-1)
