import sys


def check_cooc():
    cc = int(input())
    child_arr = list(map(int, sys.stdin.readline().rstrip().split()))
    cookc= int(input())
    c_sizes = list(map(int, sys.stdin.readline().rstrip().split()))

    child_arr.sort()
    c_sizes.sort()

    j = 0
    count = 0
    for i in range(len(child_arr)):
        greed = child_arr[i]
        while j < len(c_sizes):
            size = c_sizes[j]
            j += 1
            if size >= greed:
                count += 1
                break

    print(count)


if __name__ == '__main__':
    check_cooc()
    