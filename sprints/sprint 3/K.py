def merge(arr, left, mid, right):
	l, r = 0, 0
	k = left
	right_m = arr[mid:right]
	left_m = arr[left:mid]
	while left + l < mid and mid + r < right:
		if left_m[l] <= right_m[r]:

			arr[k] = left_m[l]
			l = l + 1
		else:
			arr[k] = right_m[r]
			r = r + 1
		k = k + 1
	if left + l < mid:
		while k < right:
			arr[k] = left_m[l]
			l = l + 1
			k = k + 1
	else:
		while k < right:
			arr[k] = right_m[r]
			r = r + 1
			k = k + 1
	return arr


def merge_sort(arr, left, right):
	if right - left > 1:  # базовый случай рекурсии
		mid = (left + right) // 2
		merge_sort(arr, left, mid)
		merge_sort(arr, mid, right)
		merge(arr, left, mid, right)
