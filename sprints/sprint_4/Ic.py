def max_common_segment(results1, results2):
    score_positions1 = {}
    max_length = 0

    for idx, score in enumerate(results1):
        if score not in score_positions1:
            score_positions1[score] = []
        score_positions1[score].append(idx)

    for idx, score in enumerate(results2):
        if score in score_positions1:
            positions = score_positions1[score]
            start_idx = 0
            for pos in positions:
                while start_idx < len(results2) and results2[start_idx] != score:
                    start_idx += 1
                if start_idx < len(results2) and results2[start_idx] == score:
                    curr_length = 1
                    i, j = start_idx, pos
                    while i + 1 < len(results2) and j + 1 < len(results1) and results2[i + 1] == results1[j + 1]:
                        curr_length += 1
                        i += 1
                        j += 1
                    max_length = max(max_length, curr_length)

    return max_length

# Чтение входных данных
n = int(input())
results1 = list(map(int, input().split()))

m = int(input())
results2 = list(map(int, input().split()))

# Вычисление и вывод результата
print(max_common_segment(results1, results2))