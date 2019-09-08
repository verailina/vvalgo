"""Implementation of merge sort algorithm."""
from typing import Sequence, NamedTuple


def merge(left_array: Sequence[int],
          right_array: Sequence[int]) -> Sequence[int]:
    """Merge two sorted array keeping sorted order.

    Args:
        left_array (Sequence[int]): First sorted array to merge.
        right_array (Sequence[int]): Second sorted array to merge.

    Returns:
        Sequence[int]: Merged array.
    """
    left_i, right_i, result_i = 0, 0, 0
    result = [0 for i in range(len(left_array) + len(right_array))]
    while left_i < len(left_array) and right_i < len(right_array):
        if left_array[left_i] < right_array[right_i]:
            result[result_i] = left_array[left_i]
            left_i += 1
        else:
            result[result_i] = right_array[right_i]
            right_i += 1
        result_i += 1

    while left_i < len(left_array):
        result[result_i] = left_array[left_i]
        left_i += 1
        result_i += 1

    while right_i < len(right_array):
        result[result_i] = right_array[right_i]
        right_i += 1
        result_i += 1
    return result


def merge_sort(array: Sequence[int]) -> Sequence[int]:
    """Sort input array by applying merge sort method.
    Args:
        array(Sequence[int]): Array to sort.

    Returns:
        Sequence[int]: Sorted array.
    """
    if len(array) <= 1:
        return array

    middle = len(array) // 2
    left = merge_sort(array[:middle])
    right = merge_sort(array[middle:])
    return merge(left, right)


class SortedArray(NamedTuple):
    """Sorted array and the number of inversions that it contains."""
    array: Sequence[int]
    """Sequence[int]: Sorted array."""
    n_inversions: int
    """int: Inversions number."""


def merge_count(left: SortedArray,
                right: SortedArray) -> SortedArray:
    """Merge two sorted arrays and count the total number of inversions.

    Args:
        left (SortedArray): First array to merge.
        right (SortedArray): Second array to merge.

    Returns:
        SortedArray: Sorted array with the total number of inversions.
    """
    left_array, right_array = left.array, right.array
    left_i, right_i, result_i = 0, 0, 0
    result_array = [0 for i in range(len(left_array) + len(right_array))]
    n_inversions = left.n_inversions + right.n_inversions

    while left_i < len(left_array) and right_i < len(right_array):
        if left_array[left_i] > right_array[right_i]:
            result_array[result_i] = right_array[right_i]
            right_i += 1
        else:
            result_array[result_i] = left_array[left_i]
            n_inversions += right_i
            left_i += 1
        result_i += 1

    while left_i < len(left_array):
        result_array[result_i] = left_array[left_i]
        left_i += 1
        result_i += 1
        n_inversions += len(right_array)

    while right_i < len(right_array):
        result_array[result_i] = right_array[right_i]
        right_i += 1
        result_i += 1

    return SortedArray(result_array, n_inversions)


def merge_sort_count(array: Sequence[int]) -> SortedArray:
    """Count number of inversions in the input array and sort it."""
    if len(array) <= 1:
        return SortedArray(array, 0)

    middle = len(array) // 2
    left = merge_sort_count(array[:middle])
    right = merge_sort_count(array[middle:])
    return merge_count(left, right)

