def bubble_sort(numbers):
    for _ in range(len(numbers) - 1):
        flag = 0
        for i in range(len(numbers) - 1):
            if numbers[i] > numbers[i + 1]:
                numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]
                flag = 1

        if flag == 0 and _ == 0:
            print(' '.join(map(str, numbers)))
            break
        if flag == 0:
            break
        print(' '.join(map(str, numbers)))


if __name__ == "__main__":
    n = input()
    values = list(map(int, input().strip().split()))
    bubble_sort(values)

