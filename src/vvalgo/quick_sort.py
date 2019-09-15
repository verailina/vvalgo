"""Implementation of quick sort algorithm."""
from typing import Sequence, Optional
from enum import Enum


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


class PivotType(Enum):
    First = "first"
    Last = "Last"
    Median = "Median"


def median_pos(a: int, b: int, c: int) -> int:
    """Find position of median of three integers.

    Args:
        a (int): First integer.
        b (int): Second integer.
        c (int): Third integer.

    Returns:
        int: Position of median value: 0 ~ a, 1 ~ b, 2 ~ c.
    """
    if c <= a <= b or b <= a <= c:
        return 0
    if a <= b <= c or c <= b <= a:
        return 1
    if a <= c <= b or b <= c <= a:
        return 2


def quick_sort(array: Sequence[int],
               left: int = 0,
               right: Optional[int] = None,
               pivot_type: PivotType = PivotType.First) -> int:
    """Quick sort algorithm for sorting an array of integers.

    Args:
        array (Sequence[int]): Input array to sort.
        left (int, optional, default 0): Left array bound.
        right (int or None, optional, default None): Right array bound.
        pivot_type (PivotType, optional, default PivotType.First): Type of
            pivot selection.

    Returns:
        int: Number of comparisons made by all recursive calls.
    """
    if len(array) <= 1:
        return 0

    if right is None:
        right = len(array) - 1

    if pivot_type is PivotType.Last:
        array[left], array[right] = array[right], array[left]

    elif pivot_type is PivotType.Median:
        size = right - left + 1
        middle = size // 2 - 1 if size % 2 == 0 else size // 2
        middle = left + middle
        median = median_pos(array[left], array[right], array[middle])
        median = [left, right, middle][median]
        array[median], array[left] = array[left], array[median]

    n_comparisons = (right - left + 1) - 1

    pivot_pos = partition(array, left, right)
    if pivot_pos - 1 > left:
        n_comparisons += quick_sort(array, left, pivot_pos - 1,
                                    pivot_type=pivot_type)
    if pivot_pos + 1 < right:
        n_comparisons += quick_sort(array, pivot_pos + 1, right,
                                    pivot_type=pivot_type)

    return n_comparisons

