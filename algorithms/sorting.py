"""
Sorting Algorithms Implementation
"""

import time


def bubble_sort(arr, key="points"):
    """Bubble Sort - O(n²)"""
    sorted_arr = arr.copy()
    n = len(sorted_arr)
    start_time = time.perf_counter()

    for i in range(n - 1):
        for j in range(n - i - 1):
            if sorted_arr[j][key] < sorted_arr[j + 1][key]:
                sorted_arr[j], sorted_arr[j + 1] = (
                    sorted_arr[j + 1],
                    sorted_arr[j],
                )

    execution_time = (time.perf_counter() - start_time) * 1000
    return sorted_arr, execution_time


def quick_sort(arr, key="points"):
    """Quick Sort - O(n log n)"""
    start_time = time.perf_counter()

    def _quick_sort(items):
        if len(items) <= 1:
            return items
        pivot = items[len(items) // 2]
        left = [x for x in items if x[key] > pivot[key]]
        middle = [x for x in items if x[key] == pivot[key]]
        right = [x for x in items if x[key] < pivot[key]]
        return _quick_sort(left) + middle + _quick_sort(right)

    sorted_arr = _quick_sort(arr.copy())
    execution_time = (time.perf_counter() - start_time) * 1000
    return sorted_arr, execution_time


def merge_sort(arr, key="points"):
    """Merge Sort - O(n log n)"""
    start_time = time.perf_counter()

    def _merge(left, right):
        result = []
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i][key] >= right[j][key]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result.extend(left[i:])
        result.extend(right[j:])
        return result

    def _merge_sort(items):
        if len(items) <= 1:
            return items
        mid = len(items) // 2
        left = _merge_sort(items[:mid])
        right = _merge_sort(items[mid:])
        return _merge(left, right)

    sorted_arr = _merge_sort(arr.copy())
    execution_time = (time.perf_counter() - start_time) * 1000
    return sorted_arr, execution_time


def sort_drivers(drivers, algorithm="quick", key="points"):
    """
    Sort drivers using specified algorithm

    Args:
        drivers: List of driver dictionaries
        algorithm: 'bubble', 'quick', or 'merge'
        key: Sort key ('points', 'wins', 'avgLapTime')

    Returns:
        Tuple of (sorted_drivers, execution_time_ms)
    """
    if algorithm == "bubble":
        return bubble_sort(drivers, key)
    elif algorithm == "quick":
        return quick_sort(drivers, key)
    elif algorithm == "merge":
        return merge_sort(drivers, key)
    else:
        return drivers, 0