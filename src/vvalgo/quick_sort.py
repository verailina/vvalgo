"""Implementation of quick sort algorithm."""
from typing import Sequence, Optional


def partition(array: Sequence[int],
              left: int = 0,
              right: Optional[int] = None) -> Sequence[int]:
    """Make partition for quick sort algorithm.

    Args:
        array (Sequence[int]): Input array.
        left (int, optional, default 0): Left array bound.
        right (int or None, optional, default None): Right array bound.

    Returns:
        Sequence[int]: Partitioned array.
    """
    if len(array) <= 1:
        return array
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
    return array

def quick_sort(array: Sequence[int]) -> Sequence[int]:
    pass
