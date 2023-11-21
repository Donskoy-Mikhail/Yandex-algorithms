numb = {3: 'def',
        2: 'abc',
        4: 'ghi',
        5: 'jkl',
        6: 'mno',
        7: 'pqrs',
        8: 'tuv',
        9: 'wxyz'}


def number_comb(var, numbers):
    global variants
    if len(numbers) == 1:
        for char in numb[numbers[0]]:
            variants.append(var + char)
        return variants
    for char in numb[numbers[0]]:
        number_comb(var + char, numbers[1:])


if __name__ == "__main__":
    numb_to_comb = list(map(int, [i for i in input()]))
    variants = []
    number_comb("", numb_to_comb)
    print(' '.join(variants))


