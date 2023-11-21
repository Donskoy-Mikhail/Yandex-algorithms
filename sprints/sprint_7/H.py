if __name__ == "__main__":
    n, m = map(int, input().split())

    # Считываем поле
    field = []
    for _ in range(n):
        row = input()
        field.append(list(map(int, row)))

    # Создаем двумерный массив для хранения максимального количества цветочков
    dp = [[0] * m for _ in range(n)]
    # Заполняем dp массив снизу вверх и слева направо
    for i in range(n -1, -1, -1):
        for j in range(0, m, 1):
            if i == n - 1:
                down_value = 0
            else:
                down_value = dp[i + 1][j]

            if j - 1 == -1:
                left_value = 0
            else:
                left_value = dp[i][j - 1]
            dp[i][j] = field[i][j] + max(down_value, left_value)
            print(dp)

    result = dp[0][m-1]
    print(result)