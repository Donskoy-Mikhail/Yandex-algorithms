"""
89908598

-- ПРИНЦИП РАБОТЫ --

Для того чтобы проводить поиск по ключу за линейное время
были определены три основные функии в классе HashTable:

get - позволяет за контантное время найти значение

put - позволяет за контантное время положить значение по ключу

delete - позволяет за контантное время удалить значение по ключу

Из моментов общих в реализации хеш функия представляет собой
просто взятие отстатка от деления нашего ключа на кол-во корзин,
за количество корзин взято простое число 100003

https://all-num.com/ru/prime/0-999999/100000-104999.html

 -- ДОКАЗАТЕЛЬСТВО КОРРЕКТНОСТИ --

Хеш функция будет равномерно распределять ключи
поскольку за количество корзин мы взяли простое число
100003 большее 10 ^ 5, что позволит более равномерно
распределять наши ключи по корзинам за счет отсутствия общих
делителей у количества корзин и ключей

Далее в алгоритме для решения коллизий используется метод цепочек
что гарантирует что если мы попали в занятую корзину то мы все равно сможем
расположить наше значение по ключу

Все три метода используют вспомогательный метод search поскольку
он нужен чтобы найти значение по ключу перебором элементов в
связном списке

Метод get работает поскольку он проверяет есть ли значение в корзине
и если оно есть то проверяет голову списка и далее если не обнаружил
ключа то продолжает искать ключ до тех пор пока не найдет ключ
и не вернет значение иначе метод выведет None

Метож put работает поскольку он проверяет есть ли  значение в корзине
и если его нет то создает голову списка и записывает в нее значение
а если метод встретил в связном списке элемент с ключем искомы то перезаписывает
значение в этом элементе иначе просто довит элемент в конец связного списка

Метод delete изет нужный ключ и если находит его то удаляет элемент из связного
списка и переопределяет порядок соседник элементов всязном списке

Если один из методов get, put не нашел нужную корзину то он возвращает None



-- ВРЕМЕННАЯ СЛОЖНОСТЬ --

В среднем за счет равномерного распределения элементов по корзинам
мы можем утвержать что все методы работают за O(1)

-- ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ --

В целом пространственная сложность а алгоритма зависит от количества корзин и от количества записанных
в них значений, поскольку мы заранее выделяем память в массиве под корзины
То есть в целом если n - длинна выделенного массива а m - количество хранимых значений
то пространственная сложность будет:
0(n) если n > m
O(m) если n < m
Послкольку массив имеет длинну 100003 что превосходит макс длинну что указана в условии 10 ^5
то пространственная сложность 0(n)

"""
import sys

class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashTable:
    def __init__(self):
        self._size = 100003
        self._table = [None] * 100003

    def _hash(self, key):
        return key % self._size

    @staticmethod
    def search(node, item):
        previous_node = None
        head = node
        while head:
            if head.key == item:
                return head, previous_node
            previous_node = head
            head = head.next
        return None, None

    def get(self, key):
        hash_value = self._hash(key)
        if self._table[hash_value] is None:
            return None
        node = self._table[hash_value]
        result_node, _ = self.search(node, key)
        if result_node is None:
            return None
        return result_node.value

    def put(self, key, value):
        node = Node(key, value)
        hash_value = self._hash(key)
        if self._table[hash_value] is None:
            self._table[hash_value] = node
        else:
            head = self._table[hash_value]
            result_node, _ = self.search(head, key)
            if result_node is None:
                node.next = head
                self._table[hash_value] = node
            else:
                result_node.value = node.value

    def delete(self, key):
        hash_value = self._hash(key)
        head = self._table[hash_value]
        if head is None:
            return None
        result_node, prev_node = self.search(head, key)
        if result_node is None:
            return None
        next_node = result_node.next
        if prev_node is None:
            self._table[hash_value] = result_node.next
        else:
            prev_node.next = next_node.next
        return result_node.value


if __name__ == "__main__":

    hash_table = HashTable()

    for _ in range(int(sys.stdin.readline().rstrip())):
        command = sys.stdin.readline().rstrip()

        if command.startswith('put'):
            _, key, value = command.split()
            hash_table.put(int(key), int(value))
        elif command.startswith('get'):
            _, key = command.split()
            print(hash_table.get(int(key)))
        else:
            _, key = command.split()
            print(hash_table.delete(int(key)))