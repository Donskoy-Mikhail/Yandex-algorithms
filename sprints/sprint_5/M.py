def sift_up(heap, idx) -> int:
    if idx == 1:
        return 1

    parentIndex = idx // 2
    if heap[parentIndex] < heap[idx]:
        heap[parentIndex], heap[idx] = heap[idx], heap[parentIndex]
        idx = sift_up(heap, parentIndex)
        return idx
    return idx
def test():
    sample = [-1, 12, 6, 8, 3, 15, 7]
    assert sift_up(sample, 5) == 1


if __name__ == '__main__':
    test()