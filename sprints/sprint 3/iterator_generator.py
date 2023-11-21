class Stringdavatel:
    def __init__(self, string, max_iter = None):
        self.string = string
        self.max_iter = max_iter
        self.size = len(string)
        self.position = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.position < self.size:
            res = self.string[self.position]
            self.position += 1
            return res
        else:
            raise StopIteration


def sushi_eater(n):
    m = 0
    for i in range(0, n):
        yield i + m
        m += 1


if __name__ == "__main__":
    # example = Stringdavatel("love")
    # print(next(example))
    # print(next(example))
    s = sushi_eater(3)
    for j in s:
        print(j)

