def dfs(graph, start):
    n = len(graph)
    stack = [start]
    visited = ["white"] * n
    result = []

    while stack:
        vertex = stack.pop()

        if visited[vertex] == 'white':
            result.append(vertex + 1)
            visited[vertex] = 'grey'

            stack.append(vertex)
            neighbors = [v for v in graph[vertex]]
            neighbors.sort()
            for neighbor in neighbors[::-1]:
                if visited[neighbor] == "white":
                    stack.append(neighbor)
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

    result = dfs(graph, s)
    print(*result)