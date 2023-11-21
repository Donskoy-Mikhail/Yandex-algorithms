import sys


def min_banknotes(x, k, denominations):
    INF = float('inf')

    dp = [INF] * (x + 1)

    dp[0] = 0

    for denom in denominations:
        for i in range(denom, x + 1):
            dp[i] = min(dp[i], dp[i - denom] + 1)
            print(dp)

    return dp[x] if dp[x] != INF else -1


if __name__ == "__main__":
    cost = int(input())
    n_num = int(input())

    noms = list(map(int, sys.stdin.readline().rstrip().split()))

    print(min_banknotes(cost, n_num, noms))
