import sys


def perimetr():

    _ = int(input())
    sides = list(map(int, sys.stdin.readline().rstrip().split()))

    sides.sort(reverse=True)

    for i in range(len(sides) - 2):
        if sides[i] < sides[i + 1] + sides[i + 2]:
            print(sides[i] + sides[i + 1] + sides[i + 2])
            break


if __name__ == '__main__':
    perimetr()