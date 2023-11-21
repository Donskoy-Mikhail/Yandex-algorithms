

def top_sort(graph):
    n = len(graph)
    stack = []
    visited = ["white"] * n
    res = []

    def dfs(graph, start):
        stack.append(start)
        while stack:
            vertex = stack.pop()
            if visited[vertex] == 'white':

                visited[vertex] = 'grey'

                stack.append(vertex)
                neighbors = [v for v in graph[vertex]]
                neighbors.sort()

                for neighbor in neighbors[::-1]:
                    if visited[neighbor] == "white":
                        stack.append(neighbor)

            elif visited[vertex] == 'grey':
                res.append(vertex + 1)
                visited[vertex] = 'black'


    for i in range(n):
        if visited[i] == "white":
            dfs(graph, i)
    return res[::-1]


if __name__ == "__main__":

    n, m = map(int, input().split())
    graph = [[] for _ in range(n)]

    for _ in range(m):
        u, v = map(int, input().split())
        graph[u - 1].append(v - 1)

    res = top_sort(graph)
    print(*res)