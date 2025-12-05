from typing import List, Optional


def linear_search(arr: List[int], target: int) -> Optional[int]:
    """Return the index of target using linear search, or None if not found.

    Time complexity: O(n)
    """
    for idx, value in enumerate(arr):
        if value == target:
            return idx
    return None


def binary_search(arr: List[int], target: int) -> Optional[int]:
    """Return the index of target using binary search, or None if not found.

    Precondition: arr must be sorted.
    Time complexity: O(log n)
    """
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return None
