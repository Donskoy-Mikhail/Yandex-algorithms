MOD = 10 ** 9 + 7


def count_ways_to_reach_stairs(n, k):
    dp = [0] * (n + 1)
    dp[1] = 1

    for i in range(2, n + 1):
        for j in range(1, min(k, i) + 1):
            dp[i] = (dp[i] + dp[i - j]) % MOD

    return dp[n]


if __name__ == "__main__":
    n, k = map(int, input().split())

    result = count_ways_to_reach_stairs(n, k)
    print(result)