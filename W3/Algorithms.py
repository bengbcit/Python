# Algorithms
# 1. Search Algorithms

# Linear Search - O(n)
def linear_search(arr: list, target) -> int:
    for i, val in enumerate(arr):
        if val == target:
            return i
    return -1

# Binary Search - O(log n) ⚡
def binary_search(arr: list, target) -> int:
    # Note: The array must be sorted for binary search to work correctly.
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            # If the target is greater than the middle element, search in the right half
            left = mid + 1
        else:
            # If the target is less than the middle element, search in the left half
            right = mid - 1
    return -1

# 2. Sorting Algorithms

# Bubble Sort - O(n²)
def bubble_sort(arr: list) -> list:
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

# Quick Sort - O(n log n) ⚡
def quick_sort(arr: list) -> list:
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)


# 3. Algorithm Complexity
# algorithm         Best Case   Average Case    Worst Case
# Linear Search     O(1)        O(n)            O(n)
# Binary Search     O(1)        O(log n)        O(log n)
# Bubble Sort       O(n²)       O(n²)           O(n²)
# Quick Sort        O(n log n)  O(n log n)      O(n²)
# Merge Sort        O(n log n)  O(n log n)      O(n log n)
