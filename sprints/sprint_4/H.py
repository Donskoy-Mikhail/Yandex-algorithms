if __name__ == "__main__":
    a = input()
    b = input()
    countera = {}
    counterb = {}
    if len(a) != len(b):
        print('No')
    else:
        for i, char in enumerate(a):
            if char not in countera:
                countera[char] = i
            else:
                countera[char] += i
        for i, char in enumerate(b):
            if char not in counterb:
                counterb[char] = i
            else:
                counterb[char] += i
        print()
        print()
        if sorted(counterb.values()) == sorted(countera.values()):
            print('YES')
        else:
            print('NO')
