"""
Search Algorithms Implementation
"""


def binary_search(arr, target):
    """
    Binary Search - O(log n)
    Requires sorted array
    """
    sorted_arr = sorted(arr, key=lambda x: x["name"].lower())
    left, right = 0, len(sorted_arr) - 1

    while left <= right:
        mid = (left + right) // 2
        mid_name = sorted_arr[mid]["name"].lower()

        if target.lower() in mid_name:
            return sorted_arr[mid]
        elif mid_name < target.lower():
            left = mid + 1
        else:
            right = mid - 1

    return None


def linear_search(arr, target):
    """
    Linear Search - O(n)
    Works on unsorted array
    """
    for driver in arr:
        if target.lower() in driver["name"].lower():
            return driver
    return None


def search_driver(drivers, search_term, method="binary"):
    """
    Search for a driver by name

    Args:
        drivers: List of driver dictionaries
        search_term: Name to search for
        method: 'binary' or 'linear'

    Returns:
        Driver dictionary if found, None otherwise
    """
    if method == "binary":
        return binary_search(drivers, search_term)
    else:
        return linear_search(drivers, search_term)