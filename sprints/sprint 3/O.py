def find_kth_min_difference(n, areas, k):
    areas.sort()
    low, high = 0, max(areas) - min(areas)

    while low <= high:
        mid = (low + high) // 2
        count = 0
        left, right = 0, 0

        while right < n:
            while areas[right] - areas[left] > mid:
                left += 1
            count += right - left
            right += 1

        if count >= k:
            high = mid - 1
        else:
            low = mid + 1

    return low


if __name__ == "__main__":
    n = int(input())
    areas = list(map(int, input().split()))
    k = int(input())

    result = find_kth_min_difference(n, areas, k)
    print(result)