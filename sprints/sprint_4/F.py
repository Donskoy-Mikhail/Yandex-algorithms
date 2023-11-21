
def anagram_sort(strings):
    anagram_groups = {}
    for idx, s in enumerate(strings):
        # Создаем сигнатуру строки путем сортировки символов
        signature = ''.join(sorted(s))

        # Добавляем текущий индекс к группе анаграмм
        if signature in anagram_groups:
            anagram_groups[signature].append(idx)
        else:
            anagram_groups[signature] = [idx]

    return anagram_groups


if __name__ == "__main__":
    n= int(input())
    words = str(input()).split()
    anagram_groups = anagram_sort(words)

    # Выводим результат
    for group in sorted(anagram_groups.values()):
        print(' '.join(map(str, group)))