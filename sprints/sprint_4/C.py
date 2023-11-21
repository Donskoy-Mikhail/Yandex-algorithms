
def precompute_hashes(s, a, m):
    n = len(s)
    p_pow = [1]
    h = [0]

    for i in range(1, n + 1):
        p_pow.append((p_pow[i - 1] * a) % m)
        h.append((h[i - 1] * a + ord(s[i - 1])) % m)

    return h, p_pow

def substring_hash(h, p_pow, l, r, m):
    hash_value = (h[r + 1] - h[l] * p_pow[r - l + 1] + m) % m
    return hash_value


if __name__ == "__main__":
    a = int(input())
    m = int(input())
    s = input()
    t = int(input())

    hashes, p_pow = precompute_hashes(s, a, m)

    for _ in range(t):
        l, r = map(int, input().split())
        hash_value = substring_hash(hashes, p_pow, l - 1, r - 1, m)
        print(hash_value)
