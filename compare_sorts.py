# compare_sorts.py
# Empirical timing comparison: Heapsort vs Quicksort vs Merge Sort

import random
import time

from heapsort import heapsort

def quicksort(a):
    # simple recursive quicksort (for comparison)
    if len(a) <= 1:
        return a
    pivot = a[len(a) // 2]
    left = [x for x in a if x < pivot]
    mid = [x for x in a if x == pivot]
    right = [x for x in a if x > pivot]
    return quicksort(left) + mid + quicksort(right)

def mergesort(a):
    if len(a) <= 1:
        return a
    mid = len(a) // 2
    left = mergesort(a[:mid])
    right = mergesort(a[mid:])
    return merge(left, right)

def merge(left, right):
    out = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            out.append(left[i]); i += 1
        else:
            out.append(right[j]); j += 1
    out.extend(left[i:])
    out.extend(right[j:])
    return out

def time_func(name, func, data):
    start = time.perf_counter()
    func(data)
    end = time.perf_counter()
    return name, end - start

def run_case(case_name, make_data, sizes=(1000, 3000, 8000)):
    print("\nCASE:", case_name)
    print("size\tHeapsort\tQuicksort\tMergeSort")
    for n in sizes:
        base = make_data(n)

        # Heapsort sorts in-place -> copy list
        a1 = base[:]
        a2 = base[:]
        a3 = base[:]

        t1 = time_func("heapsort", lambda x: heapsort(x), a1)[1]
        t2 = time_func("quicksort", lambda x: quicksort(x), a2)[1]
        t3 = time_func("mergesort", lambda x: mergesort(x), a3)[1]

        print(f"{n}\t{t1:.5f}\t\t{t2:.5f}\t\t{t3:.5f}")

if __name__ == "__main__":
    run_case("random", lambda n: [random.randint(0, n) for _ in range(n)])
    run_case("sorted", lambda n: list(range(n)))
    run_case("reverse-sorted", lambda n: list(range(n, 0, -1)))
