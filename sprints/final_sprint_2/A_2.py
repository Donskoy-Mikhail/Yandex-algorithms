"""
89213285

-- ПРИНЦИП РАБОТЫ --
Пускай head будет указывать на первый элемент а tail на последний
Далее проинициизируем их так чтобы head был на 0 позиции а tail n - 1

Идея в том что мы держим указатели впереди (позади для вставки в конец) ячейки
 в которые будем записывать значения и перемещать их вперед (назад) если добавляем элемент
 и  перемещаем назад (вперед) если удаляем элемент
 
 -- ДОКАЗАТЕЛЬСТВО КОРРЕКТНОСТИ --
За счет того что мы передвигам указатели вперед (назад) только если размер дека не превышает
максимальный размер мы можем быть спокойны за то что не произойдет  переписывание уже занятых ячеек
Также прежде чем вытащить элемент мы проверяем не пустой ли дек что позволяет нам обработать случай
некорректного вызова методов pop на пустом буфере
Далее размещение указателей на соседние позиции позволяет обработать случаи когда например сначала мы добавлили
элемент вперед и дека и потом попробовали удалить его с конца что также гарантирует что при последовательном вызове
push_front и push_back позволит избежать перезаписывания существуещего в буфере значения

В стандатрных ситуациях не описанных выше алогритм работает без ошибок за счет двух указателей к которым привязаны
операции добавления и извечения как с начала так и с конца

-- ВРЕМЕННАЯ СЛОЖНОСТЬ --
Все операции выполняются за O(1) поскольку они выполняются за счет индексов массива
поиск по которым занимает константное время

-- ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ --
Массив для буфера содержит n элементов также используется переменные  для текущего размера массива
максимального размера и два указателя и в целом они занимают константную память
Итог: O(n) + O(1) = O(n) памяти 
"""


class Deque:
    def __init__(self, n):
        self._queue = [None] * n
        self._max_n = n
        self._head = 0
        self._tail = n - 1
        self._size = 0

    @property
    def is_empty(self):
        return self._size == 0

    def push_front(self, x):
        if self._size != self._max_n:
            self._queue[self._head] = x
            self._head = (self._head + 1) % self._max_n
            self._size += 1
        else:
            raise Exception("deque is_empty")

    def pop_front(self):
        if self.is_empty:
            raise Exception("deque is_empty")
        else:
            self._head = (self._head - 1) % self._max_n
            x = self._queue[self._head]
            self._queue[self._head] = None
            self._size -= 1
            print(x)

    def push_back(self, x):
        if self._size != self._max_n:
            self._queue[self._tail] = x
            self._tail = (self._tail - 1) % self._max_n
            self._size += 1
        else:
            raise Exception("deque is_empty")

    def pop_back(self):
        if self.is_empty:
            raise Exception("deque is_empty")
        else:
            self._tail = (self._tail + 1) % self._max_n
            x = self._queue[self._tail]
            self._queue[self._tail] = None
            self._size -= 1
            print(x)


if __name__ == "__main__":
    num_com = int(input())
    max_size = int(input())
    queue_ = Deque(max_size)
    for _ in range(num_com):
        inp = str(input()).split()
        try:
            if inp[0] == "pop_front":
                queue_.pop_front()
            elif inp[0] == "push_front":
                queue_.push_front(int(inp[1]))
            elif inp[0] == "push_back":
                queue_.push_back(int(inp[1]))
            elif inp[0] == "pop_back":
                queue_.pop_back()
        except Exception as e:
            print("error")
