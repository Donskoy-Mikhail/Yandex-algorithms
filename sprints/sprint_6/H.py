def dfs(graph, start):
    n = len(graph)
    stack = [start]
    visited = ["white"] * n
    time = None
    entry = [None] * n
    leave = [None] * n
    while stack:
        vertex = stack.pop()
        if visited[vertex] == 'white':
            if time is None:
                time = 0
            else:
                time += 1

            entry[vertex] = time
            visited[vertex] = 'grey'

            stack.append(vertex)
            neighbors = [v for v in graph[vertex]]
            neighbors.sort()

            for neighbor in neighbors[::-1]:
                if visited[neighbor] == "white":
                    stack.append(neighbor)

        elif visited[vertex] == 'grey':
            time += 1
            leave[vertex] = time
            visited[vertex] = 'black'

    return entry, leave


if __name__ == "__main__":

    n, m = map(int, input().split())
    graph = [[] for _ in range(n)]

    for _ in range(m):
        u, v = map(int, input().split())
        graph[u - 1].append(v - 1)

    entry, leave = dfs(graph, 1-1)
    for i, j in zip(entry, leave):
        print(i,j)