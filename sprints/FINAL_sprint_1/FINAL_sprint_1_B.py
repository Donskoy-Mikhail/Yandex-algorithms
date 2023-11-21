# B 89093018

from collections import Counter


def read_input():
	k = int(input()) * 2
	hash_map = Counter()
	t = 0
	for i in range(4):
		hash_map.update(Counter(list(map(str, input()))))

	for key, v in hash_map.items():
		if key != '.' and v <= k:
			t += 1

	return t


if __name__ == "__main__":
	print(read_input())
