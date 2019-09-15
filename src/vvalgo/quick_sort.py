"""Implementation of quick sort algorithm."""
from typing import Sequence, Optional


def partition(array: Sequence[int],
              left: int = 0,
              right: Optional[int] = None) -> int:
    """Make partition for quick sort algorithm.

    Args:
        array (Sequence[int]): Input array.
        left (int, optional, default 0): Left array bound.
        right (int or None, optional, default None): Right array bound.

    Returns:
        int: Index of pivot element in partitioned array.
    """
    if len(array) <= 1:
        return 0
    if right is None:
        right = len(array) - 1

    if (left > right or left < 0 or right < 0
            or left >= len(array) or right >= len(array)):
        raise ValueError(f"invalid array bounds: left={left}, right={right}")

    pivot = array[left]
    i = left + 1
    j = left + 1
    while j <= right:
        if array[j] < pivot:
            array[i], array[j] = array[j], array[i]
            i += 1
        j += 1
    array[left], array[i - 1] = array[i - 1], array[left]
    return i - 1


def quick_sort(array: Sequence[int],
               left: int = 0,
               right: Optional[int] = None) -> int:
    """Quick sort algorithm for sorting an array of integers.

    Args:
        array (Sequence[int]): Input array to sort.
        left (int, optional, default 0): Left array bound.
        right (int or None, optional, default None): Right array bound.

    Returns:
        int: Number of comparisons made by all recursive calls.
    """
    if len(array) <= 1:
        return 0

    if right is None:
        right = len(array) - 1

    n_comparisons = (right - left + 1) - 1
    pivot_pos = partition(array, left, right)
    if pivot_pos - 1 > left:
        n_comparisons += quick_sort(array, left, pivot_pos - 1)
    if pivot_pos + 1 < right:
        n_comparisons += quick_sort(array, pivot_pos + 1, right)

    return n_comparisons

