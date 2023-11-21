def merge_flowerbed(flowerbeds):
    if not flowerbeds:
        return []

    flowerbeds.sort(key=lambda x: x[0])
    res = [flowerbeds[0]]

    for cur in flowerbeds[1:]:
        last = res[-1]
        if cur[0] <= last[1]:
            last[1] = max(last[1], cur[1])
        else:
            res.append(cur)

    return res


if __name__ == "__main__":
    n = int(input())
    values = []
    for _ in range(n):
        values.append(list(map(int, input().strip().split())))
    r = merge_flowerbed(values)
    for el in r:
        print(f'{el[0]} {el[1]}')

