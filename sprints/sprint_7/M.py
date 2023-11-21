if __name__ == "__main__":
    n, m = map(int, input().split())
    dp = [[0] * (m +1) for _ in range(n)]

    field = []
    for _ in range(n):
        row = input().split()
        field.append(list(map(int, row)))

    for i in range(n):
        print(i)
        for j in range(0, m + 1):
            last_item_max = dp[i - 1][j] if i > 0 else 0
            new_item_ = field[i][1] + dp[i - 1][j - field[i][0]] if j - field[i][0] > 0 else 0
            dp[i][j] = max(last_item_max, new_item_)

    print(field)
    print(dp)