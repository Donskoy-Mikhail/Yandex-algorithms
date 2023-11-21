import sys


def buy_houses():
    numbers = list(map(int, sys.stdin.readline().rstrip().split()))
    _ = numbers[0]
    k = numbers[1]
    arr = list(map(int, sys.stdin.readline().rstrip().split()))

    arr.sort()

    sum_ = 0
    count = 0
    for item in arr:
        sum_ += item
        if sum_ > k:
            break
        else:
            count += 1

    print(count)


if __name__ == '__main__':
    buy_houses()