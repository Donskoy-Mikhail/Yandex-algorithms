def merge(array, left, mid, right):
    left_array = array[left:mid]
    right_array = array[mid:right]

    i, j, k = 0, 0, left

    while i < len(left_array) and j < len(right_array):
        if left_array[i] <= right_array[j]:
            array[k] = left_array[i]
            i += 1
        else:
            array[k] = right_array[j]
            j += 1
        k += 1

    while i < len(left_array):
        array[k] = left_array[i]
        i += 1
        k += 1

    while j < len(right_array):
        array[k] = right_array[j]
        j += 1
        k += 1

    return array


def merge_sort(array, begin, end):
    if end - begin <= 1:
        return

    mid = (begin + end) // 2

    merge_sort(array, begin, mid)
    merge_sort(array, mid, end)
    array = merge(array, begin, mid, end)

