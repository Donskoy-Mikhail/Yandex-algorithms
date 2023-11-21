from collections import deque


def bfs(graph, start):
    n = len(graph)
    qeuque = deque()
    visited = ["white"] * n
    max_distance = -1  # Изначально максимальное расстояние равно -1

    qeuque.append(start)
    visited[start] = 'grey'
    distance = 0

    while qeuque:
        # Обход в ширину уровня графа
        level_size = len(qeuque)
        for _ in range(level_size):
            vertex = qeuque.popleft()

            neighbors = [v for v in graph[vertex]]
            neighbors.sort()

            for neighbor in neighbors:
                if visited[neighbor] == "white":
                    qeuque.append(neighbor)
                    visited[neighbor] = 'grey'

        # Увеличиваем расстояние на каждом уровне
        distance += 1

        # Обновляем максимальное расстояние
        max_distance = distance

    return max_distance - 1


if __name__ == "__main__":
    n, m = map(int, input().split())
    graph = [[] for _ in range(n)]

    for _ in range(m):
        u, v = map(int, input().split())
        graph[u - 1].append(v - 1)
        graph[v - 1].append(u - 1)

    s = int(input()) - 1

    result = bfs(graph, s)
    print(result)
