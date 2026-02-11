# heapsort.py
# Assignment 4: Heapsort implementation (max-heap)

def heapify(a, n, i):
    # maintain max-heap property for subtree rooted at i
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and a[left] > a[largest]:
        largest = left
    if right < n and a[right] > a[largest]:
        largest = right

    if largest != i:
        a[i], a[largest] = a[largest], a[i]
        heapify(a, n, largest)

def heapsort(a):
    n = len(a)

    # build max-heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(a, n, i)

    # extract max one by one
    for end in range(n - 1, 0, -1):
        a[0], a[end] = a[end], a[0]
        heapify(a, end, 0)

    return a

if __name__ == "__main__":
    data = [5, 3, 8, 4, 1, 2]
    print("Original:", data)
    heapsort(data)
    print("Sorted:  ", data)
