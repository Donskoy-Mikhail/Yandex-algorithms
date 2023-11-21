if __name__ == "__main__":
    
    n, m = map(int, input().split())

    adjacency_matrix = [[0] * n for _ in range(n)]

    for _ in range(m):
        u, v = map(int, input().split())
        adjacency_matrix[u - 1][v - 1] = 1

    for row in adjacency_matrix:
        print(*row)