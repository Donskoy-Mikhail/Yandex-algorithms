"""
92492007

-- ПРИНЦИП РАБОТЫ --

Идея решения состоит в том чтобы свести задачу к поиску циклов в графе

 -- ДОКАЗАТЕЛЬСТВО КОРРЕКТНОСТИ --

Решения корректное за счет того что мы хитрым способом строим список смежности графа
работает это так - у нас есть два типа дорог и если мы будем при построении ориентированного графа
задавать одним типам дорог направление как оно и должно быть то есть от города изначального до конечного
а другим наоборот от конечного до начального то получившийся граф будет иметь циклы только тогда когда
будет существовать такой путь что "если существуют пары городов A и B такой, что от A до B можно добраться как по дорогам типа R, так и по дорогам типа B"


-- ВРЕМЕННАЯ СЛОЖНОСТЬ --

Временная сложность алгоритма также зависит от размера входного графа
В худшем случае, если в графе отсутствуют циклы то мы будем выполнять DFS для каждой вершины
и это будет иметь временную сложность O(V+E),
где V - количество вершин, а E - количество рёбер в графе.

-- ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ --

Пространственная сложность зависит от списков смежности - O(V + E)
+
также нужно учесть что мы храним список посещенных вершин O(V)
Итогавая сложность это O(V + E)

"""


def has_cycle(graph):
    def dfs(graph, start, visited):
        stack = [start]
        while stack:
            vertex = stack.pop()

            if visited[vertex] == 'white':
                visited[vertex] = 'grey'

                stack.append(vertex)

                for neighbor in graph[vertex]:
                    if visited[neighbor] == "white":
                        stack.append(neighbor)
                    elif visited[neighbor] == "grey":
                        return True
            elif visited[vertex] == 'grey':
                visited[vertex] = "black"

        return False

    visited = ["white"] * len(graph)
    for city in range(len(graph)):
        if dfs(graph, city, visited):
            return True
    return False


if __name__ == "__main__":
    n = int(input())
    graph = {node: [] for node in range(n)}

    for i in range(n - 1):
        for j, node in enumerate(str(input())):
            if node == 'R':
                graph[i].append(i + j + 1)
            else:
                graph[i + j + 1].append(i)
    if has_cycle(graph):
        print("NO")
    else:
        print("YES")
