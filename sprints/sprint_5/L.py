def sift_down(heap, idx) -> int:
    left = 2 * idx
    right = 2 * idx + 1

    if len(heap) <= left:
        return idx

    index_largest = right if right < len(heap) and heap[left] < heap[right] else left

    if heap[idx] < heap[index_largest]:
        heap[idx], heap[index_largest] = heap[index_largest], heap[idx]
        idx = sift_down(heap, index_largest)
    return idx

def test():
    sample = [-1, 12, 1, 8, 3, 4, 7]

    assert sift_down(sample, 2) == 5


if __name__ == '__main__':
    test()