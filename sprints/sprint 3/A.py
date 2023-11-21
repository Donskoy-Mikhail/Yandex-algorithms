n = int(input())
res = []


def comb_branch(s, count_left, count_right):
    if 2 * n == len(s):
        return res.append(s)

    if count_left < n:
        comb_branch(s + "(", count_left + 1, count_right)
    if count_right < count_left:
        comb_branch(s + ")", count_left, count_right + 1)


comb_branch('', 0, 0)

for i in res:
    print(i)
