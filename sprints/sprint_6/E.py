

def components(graph):
    n = len(graph)
    stack = []
    color = [-1] * n
    component_count = 0

    def dfs(graph, start):
        stack.append(start)
        while stack:
            vertex = stack.pop()
            if color[vertex] == -1:

                color[vertex] = 'grey'

                stack.append(vertex)
                neighbors = [v for v in graph[vertex]]
                neighbors.sort()

                for neighbor in neighbors[::-1]:
                    if color[neighbor] == -1:
                        stack.append(neighbor)

            elif color[vertex] == 'grey':
                color[vertex] = component_count

    for i in range(n):
        if color[i] == -1:
            dfs(graph, i)
            component_count += 1
    return component_count, color


if __name__ == "__main__":

    n, m = map(int, input().split())
    graph = [[] for _ in range(n)]

    for _ in range(m):
        u, v = map(int, input().split())
        graph[u - 1].append(v - 1)
        graph[v - 1].append(u - 1)

    component_count, color = components(graph)
    print(component_count)
    for i in range(0, component_count + 1):
        res = []
        for j, el in enumerate(color):
            if el == i:
                res.append(j + 1)
        print(*res)