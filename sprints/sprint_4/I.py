def max_common_segment(n, m, results1, results2):
    positions = {}  # Хранение позиций для каждого очка

    for idx, score in enumerate(results1):
        if score in positions:
            positions[score].append(idx)
        else:
            positions[score] = [idx]

    max_length = 0
    for idx, score in enumerate(results2):
        if score in positions and m - idx > max_length:

            for j in positions[score]:
                max_length_here = 1
                i = idx + 1
                j += 1
                while j < n and i < m and results1[j] == results2[i] :
                    max_length_here += 1
                    i += 1
                    j += 1
                max_length = max(max_length, max_length_here)

    return max_length


if __name__ == "__main__":
    # Чтение входных данных
    n = int(input())
    results1 = list(map(int, input().split()))

    m = int(input())
    results2 = list(map(int, input().split()))

    # Вычисление и вывод результата
    print(max_common_segment(n, m, results1, results2))