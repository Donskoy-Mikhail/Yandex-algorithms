n = int(input())
m = int(input())
nums1 = list(map(int, input().split()))
nums1 += list(map(int, input().split()))

nums1.sort()

fl= n + m

if fl % 2 != 0:
    print(nums1[fl//2])
else:
    print((nums1[fl//2 - 1] + nums1[fl//2])/2)

