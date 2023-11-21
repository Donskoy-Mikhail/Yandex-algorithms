n = int(input())
m = int(input())
nums1 = list(map(int, input().split()))
nums2 = list(map(int, input().split()))

if n > m:
    nums1, nums2, n, m = nums2, nums1, m, n

imin, imax, half_len = 0, n, (n + m + 1) // 2
while imin <= imax:
    i = (imin + imax) // 2
    j = half_len - i
    if i < n and nums2[j - 1] > nums1[i]:
        imin = i + 1
    elif i > 0 and nums1[i - 1] > nums2[j]:
        imax = i - 1
    else:

        max_of_left = 0
        if i == 0:
            max_of_left = nums2[j - 1]
        elif j == 0:
            max_of_left = nums1[i - 1]
        else:
            max_of_left = max(nums1[i - 1], nums2[j - 1])

        if (n + m) % 2 == 1:
            print(max_of_left)
            break

        min_of_right = 0
        if i == n:
            min_of_right = nums2[j]
        elif j == m:
            min_of_right = nums1[i]
        else:
            min_of_right = min(nums1[i], nums2[j])

        print((max_of_left + min_of_right) / 2)
        break

