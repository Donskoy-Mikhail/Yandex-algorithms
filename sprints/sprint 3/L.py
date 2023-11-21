def bicycle():
    n = int(input())
    cum_sum = list(map(int, input().rstrip().split()))
    price = int(input())
    left = 0
    right = n - 1
    ans = [-1, -1]
    tmp = None
    tmp_2 = None
    while left < right:

        if cum_sum[(left + right) // 2] >= price:
            tmp = (left + right) // 2 + 1
            right = (left + right) // 2 - 1
        else:
            left = (left + right) // 2 + 1

    if tmp:
        ans[0] = tmp
        price = price + price

    if ans[0] != -1:
        right = n - 1
        while left <= right:
            if cum_sum[(left + right) // 2] >= price:
                tmp_2 = (left + right) // 2 + 1
                right = (left + right) // 2 - 1
            else:
                left = (left + right) // 2 + 1

    if tmp_2:
        ans[1] = tmp_2

    print(*ans)


if __name__ == "__main__":
    bicycle()
