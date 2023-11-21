def outer(s=1):
    def multimple(func):
        count = 0
        def wrapper(x):
            nonlocal count
            count += 1
            res = (func(x) - count) * s
            return res
        return wrapper
    return multimple


@outer(0)
def sush(x):
    return x * 2


print(sush(2))
print(sush(2))
print(sush(2))
