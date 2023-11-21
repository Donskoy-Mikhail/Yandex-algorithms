import sys


def trade_max(curs):
    n = len(curs)
    id_stock = None
    profit = 0
    for idx in range(len(curs)):
        if id_stock is None:
            if idx + 1 <= n - 1 and curs[idx] < curs[idx + 1]:
                id_stock = idx
        elif idx + 1 == n or curs[idx] > curs[idx + 1]:
            profit += curs[idx] - curs[id_stock]
            id_stock = None
    return profit


if __name__ == "__main__":
    n = int(sys.stdin.readline().rstrip())

    history = []
    history.extend(list(map(int, sys.stdin.readline().rstrip().split())))

    print(trade_max(history))
