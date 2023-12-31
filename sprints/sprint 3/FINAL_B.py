"""
89514788


-- ПРИНЦИП РАБОТЫ --
В реализации используется две ключевые идеи in-place quick sort и
использование функции для сравнения элементов именнно таким способом что
определил Тимофей

В целом сама функция сортировки вызывает функцию которая переупорядочивает
массив относительного опорного элемента и далее вызывает себя рекурсивно относительно опроного элемента
как справа так и слева, сама функция что упорядочивает массив основана на идее что описана в условии
задачи и дополнительно использует функцию compare что помогает определить какой элемент больше
из двух


 -- ДОКАЗАТЕЛЬСТВО КОРРЕКТНОСТИ --
За счет того что алгоритм переставляет элементы вокруг опорного
(по принципу меньше больше опорного) до тех пока указатели не сойдутся
позволяет отсортировать массив, также алгоритм правильно работает за счет
того что опредена функция что явно указывает на порядок элементов и делает она
это следующим образом:

если числа решенных задач разные, то мы просто возвращаем разницу между этими числами
(чтобы участник с большим числом решенных задач шел выше). Если числа решенных задач
одинаковы, мы сравниваем их по размеру штрафа, возвращая разницу между штрафами
(чтобы участник с меньшим штрафом шел выше). Если и штрафы одинаковы, мы сравниваем
 их логины и возвращаем -1, если первый логин меньше, и 1, если первый логин больше
(чтобы логины шли в алфавитном порядке).

Таким образом опираясь на то что quick sort позволяет отсортировать массив
и на то что мы задали функцию для определения порядка элементов которую
мы используем в partition мы можем утверждать
что данный подход корректен


-- ВРЕМЕННАЯ СЛОЖНОСТЬ --
Алгоритм работает за то же время что и quick sort то есть
в среднем за O(n log n) и в худшем за O(n^2)


-- ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ --
Кроме хранения самого массива O(n) потребутеся хранить стек вызовов -
что означает что дополнительная память может потребоваться в обьеме
в среднем O(log n) и в худшем случае O(n)
"""


def quick_sort(arr, low, high):
    if low < high:
        pivot_index = partition(arr, low, high)
        quick_sort(arr, low, pivot_index - 1)
        quick_sort(arr, pivot_index + 1, high)


def partition(arr, low, high):
    support = arr[high]
    i = low
    j = high - 1

    while True:
        while i <= j and compare(arr[i], support) < 0:
            i += 1
        while j >= i and compare(arr[j], support) > 0:
            j -= 1

        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
        else:
            break

    arr[i], arr[high] = arr[high], arr[i]
    return i


def compare(participant1, participant2):
    if participant1[1] != participant2[1]:
        return participant2[1] - participant1[1]
    elif participant1[2] != participant2[2]:
        return participant1[2] - participant2[2]
    else:
        return -1 if participant1[0] < participant2[0] else 1


if __name__ == "__main__":
    n = int(input())
    participants = []
    for _ in range(n):
        login, solved_tasks, penalty = input().split()
        solved_tasks = int(solved_tasks)
        penalty = int(penalty)
        participants.append((login, solved_tasks, penalty))

    quick_sort(participants, 0, n - 1)

    for participant in participants:
        print(participant[0])


