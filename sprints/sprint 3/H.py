from functools import reduce
from functools import cmp_to_key

def comp(a, b):
    if a + b < b + a:
        return -1
    elif a + b > b + a:
        return 1
    else:
        return 0
if __name__ == "__main__":
    n = input()
    values = list(map(str, input().strip().split()))
    res = reduce(lambda x, y: x + y, map(str,  sorted(values, key=cmp_to_key(comp), reverse=True)))
    print(res)

