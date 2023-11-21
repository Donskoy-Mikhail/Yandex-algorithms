if __name__ == "__main__":
    counter = set()
    n = int(input())
    for i in range(n):
        el = str(input())
        if el not in counter:
            counter.add(el)
            print(el)
