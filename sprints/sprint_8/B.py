def levenshtein_distance(a, b):
    l_a = len(a)
    l_b = len(b)

    p_a = 0
    p_b = 0

    errors_count = 0

    while True:
        if l_a == p_a + 1:
            break
        if l_b == p_b + 1:
            break

        if a[p_a] == b[p_b]:
            p_a += 1
            p_b += 1
            continue
        else:
            errors_count += 1

            if a[p_a + 1] == b[p_b + 1]:
                p_a += 1
                p_b += 1
                continue
            if a[p_a + 1] == b[p_b]:
                p_a += 1
                continue
            if b[p_b + 1] == a[p_a]:
                p_b += 1
                continue
            errors_count += 1
            break

    errors_count += (l_a - p_a - 1)
    errors_count += (l_b - p_b - 1)
    return errors_count


if __name__ == "__main__":
    passport_name = input().strip()
    database_name = input().strip()

    distance = levenshtein_distance(passport_name, database_name)

    if distance <= 1:
        print("OK")
    else:
        print("FAIL")