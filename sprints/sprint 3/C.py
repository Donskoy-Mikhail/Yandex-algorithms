def is_substr(a, b):
    i = 0
    k = 0
    for char in a:
        while i < len(b):
            if b[i] == char:
                i += 1
                k += 1
                break
            else:
                i += 1
    return True if k == len(a) else False


if __name__ == "__main__":
    substr = str(input())
    str_ = str(input())
    print(is_substr(substr, str_))
