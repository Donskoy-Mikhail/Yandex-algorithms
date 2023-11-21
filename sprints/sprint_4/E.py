"""
На вход подается строка.
Нужно определить длину наибольшей подстроки,
которая не содержит повторяющиеся символы.
"""


def longest_substring(str_):
    max_size = 0
    current_size = 0
    string = ''
    for char in str_:
        if char not in string:
            string += char
            current_size += 1
            max_size = max(max_size, current_size)
        else:
            while char in string:
                string = string[1:]
                current_size -= 1
            string += char
            current_size += 1

    return max_size


if __name__ == '__main__':
    string = input()
    print(longest_substring(string))