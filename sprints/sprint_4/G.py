def longest_draw_segment(n, results):
    max_length = 0  # Инициализируем максимальную длину сегмента
    current_length = 0  # Инициализируем текущую длину сегмента
    prefix_sum = 0  # Инициализируем кумулятивную сумму баллов

    # Создаём словарь для хранения индекса первого появления каждой кумулятивной суммы
    sum_indices = {}

    # Проходимся по результатам раундов
    for i in range(n):

        print("-----------------------")
        print(i)
        result = results[i] * 2 - 1  # Преобразуем результат: 0 становится -1, а 1 становится 1
        prefix_sum += result  # Обновляем кумулятивную сумму баллов

        # Если текущая кумулятивная сумма была ранее замечена
        if prefix_sum in sum_indices:
            print(True)
            print(prefix_sum," prefix_sum")
            print(current_length," current_length")
            print(sum_indices," sum_indices")
            current_length = i - sum_indices[prefix_sum]  # Рассчитываем текущую длину сегмента
            print(current_length," current_length")
            max_length = max(max_length, current_length)  # Обновляем максимальную длину сегмента
            print(max_length," max_length")
        else:
            sum_indices[prefix_sum] = i  # Сохраняем индекс первого появления кумулятивной суммы
            print(sum_indices," sum_indices")
    return max_length  # Возвращаем длину наибольшего сегмента


if __name__ == "__main__":
    rounds = int(input())
    res = list(map(int, input().rstrip().split()))
    print(longest_draw_segment(rounds, res))
