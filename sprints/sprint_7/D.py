def fib(num):
    dp = []
    dp.extend([1, 1])
    for i in range(2, num + 1):
        dp.append((dp[i - 1] + dp[i - 2]) % (10**9 + 7))

    return dp[n]


if __name__ == "__main__":
    n = int(input())
    print(fib(n))
