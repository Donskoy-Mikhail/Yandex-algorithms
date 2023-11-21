def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)


def catalan_number(n):
    return factorial(2 * n) // (factorial(n) * factorial(n + 1))


if __name__ == "__main__":
    n = int(input())
    print(catalan_number(n))