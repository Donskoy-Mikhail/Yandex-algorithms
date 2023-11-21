# A 89092883

from typing import List, Tuple

def get_dist(number_list, n):
    if n == 0:
        return [0]
    idx_zeros = []
    res = [-1] * n
    for i in range(n):
        if number_list[i] == 0:
            res[i] = 0
            idx_zeros.append(i)
    for i in idx_zeros:
        if i == 0:
            j = 1
            while (i + j < n and number_list[i + j] != 0 
            and (j < res[i + j] or res[i + j] == -1)):
                res[i + j] = j
                j += 1
        elif i == n - 1:
            j = 1
            while (i - j >= 0 and number_list[i - j] != 0 and 
            (j < res[i - j] or res[i - j] == -1)):
                res[i - j] = j
                j += 1
        else:
            j = 1
            while (i - j >= 0 and number_list[i - j] != 0
            and (j < res[i - j] or res[i - j] == -1)):
                res[i - j] = j
                j += 1
                
            j = 1
            while (i + j < n and number_list[i + j] != 0
            and (j < res[i + j] or res[i + j] == -1)):
                res[i + j] = j
                j += 1
    return res
			
def read_input() -> Tuple[List[int], int]:
    n = int(input())
    number_list = list(map(int, input().strip().split()))
    
    return number_list, n
if __name__ == "__main__":
    number_list, n = read_input()
    print(" ".join(map(str, get_dist(number_list, n))))