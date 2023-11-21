import sys

def dijkstra(graph, start):
    n = len(graph)
    dist = [sys.maxsize] * n
    dist[start] = 0
    visited = [False] * n

    for _ in range(n):
        u = -1
        for i in range(n):
            # Поиск минимальной непосещенной вершины
            if not visited[i] and (u == -1 or dist[i] < dist[u]):
                u = i
        visited[u] = True
        # Проверяем растяние до всех соседних вершин через эту и если меньше то обновляем
        for v, weight in enumerate(graph[u]):
            if weight > 0:
                dist[v] = min(dist[v], dist[u] + weight)

    return dist

# Чтение входных данных
n, m = map(int, input().split())
graph = [[-1] * n for _ in range(n)]

for _ in range(m):
    u, v, w = map(int, input().split())
    if graph[u - 1][v - 1] == -1:
        graph[u - 1][v - 1] = w
        graph[v - 1][u - 1] = w

# Вычисление кратчайших расстояний
shortest_distances = []
for i in range(n):
    distances = dijkstra(graph, i)
    shortest_distances.append(distances)

# Вывод результатов
for row in shortest_distances:
    for distance in row:
        if distance == sys.maxsize:
            print(-1, end=" ")
        else:
            print(distance, end=" ")
    print()