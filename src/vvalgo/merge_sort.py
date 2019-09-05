"""Implementation of merge sort algorithm."""
from typing import Sequence


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
    if len(array) == 1:
        return array

    middle = len(array) // 2

