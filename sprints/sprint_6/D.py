from collections import deque


def bfs(graph, start):
    n = len(graph)
    qeuque = deque()
    visited = ["white"] * n
    result = []
    qeuque.append(start)
    while qeuque:
        vertex = qeuque.popleft()

        if visited[vertex] == 'white':
            result.append(vertex + 1)
            visited[vertex] = 'grey'

            qeuque.append(vertex)
            neighbors = [v for v in graph[vertex]]
            neighbors.sort()
            for neighbor in neighbors:
                if visited[neighbor] == "white":
                    qeuque.append(neighbor)
        elif visited[vertex] == 'grey':
            visited[vertex] = 'black'

    return result


if __name__ == "__main__":

    n, m = map(int, input().split())
    graph = [[] for _ in range(n)]

    for _ in range(m):
        u, v = map(int, input().split())
        graph[u - 1].append(v - 1)
        graph[v - 1].append(u - 1)

    s = int(input()) - 1

    result = bfs(graph, s)
    print(*result)
