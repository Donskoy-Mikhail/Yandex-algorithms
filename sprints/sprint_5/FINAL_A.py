"""
90160790

-- ПРИНЦИП РАБОТЫ --

Используем класс Participant в котором мы храним данные игроков и создаем магический метод __lt__
что позволяет нам использовать оператор < для прямого сравнения обьектов

Далее мы просто считываем данные и по очереди добавляем участника после чего
выполняем операцию sift_up что позволяет называть массив кучей

Далее мы извлекаем элементы из кучи и сразу печатаем его и далее
ставим элемент с конца в корень и вопстанавливаем свойства кучи благодаря
операции sift_down

 -- ДОКАЗАТЕЛЬСТВО КОРРЕКТНОСТИ --

На первом этапе алгоритма, для каждого участника выполняется вставка в кучу.
 При этом, сравнивая и обменивая элементы, обеспечивается соблюдение свойства кучи.

 После построения кучи, корень кучи содержит максимальный элемент. Этот элемент извлекается
 и помещается в конец массива. Затем, чтобы восстановить свойство кучи, выполняется просеивание вниз
 на корневом элементе. Это продолжается до тех пор, пока в куче не останется один элемент,
 и массив будет отсортирован в правильном порядке.

 Сравнение элементов во время просеивания вверх и вниз выполняется в соответствии с магическим методом то есть
 сначала по числу задач потом по числу штрафов  потом по лексикографическому порядку
  Следовательно, массив будет отсортирован сначала по одному критерию, затем по другому, и так далее.

-- ВРЕМЕННАЯ СЛОЖНОСТЬ --

Временная сложность определяется по сути операцией построения кучи
и операцией удаления корня

sift_down , sift_up имеют сложность O(log n)
на каждую из операций приходится n вызовов

Итоговая сложность O(n log n  +  n log n) = O(n log n)

-- ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ --

Пространственная сложность зависит от количества участников и структуры данных
В данном случае, пространственная сложность составляет O(n),

"""

class Participant:
    def __init__(self, name, tasks, fine):
        self.name = name
        self.tasks = tasks
        self.fine = fine

    def __lt__(self, other):
        if self.tasks != other.tasks:
            return self.tasks < other.tasks
        elif self.fine != other.fine:
            return self.fine > other.fine
        else:
            return self.name > other.name


def sift_down(heap, n, i):
    largest = i
    left = 2 * i
    right = 2 * i + 1

    if left >= n:
        return None

    if left < n and heap[largest] < heap[left]:
        largest = left

    if right < n and heap[largest] < heap[right]:
        largest = right

    if largest != i:
        heap[i], heap[largest] = heap[largest], heap[i]
        sift_down(heap, n, largest)


def sift_up(heap, i) -> int:
    if i == 0:
        return

    parentindex = (i) // 2
    if heap[parentindex] < heap[i]:
        heap[parentindex], heap[i] = heap[i], heap[parentindex]
        sift_up(heap, parentindex)


if __name__ =='__main__':
    n = int(input())
    participants = []

    for _ in range(n):
        name, tasks, fine = input().split()
        tasks = int(tasks)
        fine = int(fine)
        participant = Participant(name, tasks, fine)
        participants.append(participant)
        sift_up(participants, len(participants) - 1)

    while participants:
        participants[0], participants[-1] = participants[-1], participants[0]
        print(participants.pop().name)
        sift_down(participants, len(participants), 0)