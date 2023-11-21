if __name__ == "__main__":
    n, m = map(int, input().split())

    adjacency_list = [[] for _ in range(n)]

    for _ in range(m):
        u, v = map(int, input().split())
        adjacency_list[u - 1].append(v)

    for i in range(n):
        print(len(adjacency_list[i]), *adjacency_list[i])