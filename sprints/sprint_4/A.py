def calculate_polynomial_hash(s, a, m):
    hash_value = 0
    for char in s:
        hash_value = (hash_value * a + ord(char)) % m
    return hash_value


if __name__ == "__main__":
    a = int(input())
    m = int(input())
    s = input()

    # Calculate and print the hash
    res = calculate_polynomial_hash(s, a, m)
    print(res)