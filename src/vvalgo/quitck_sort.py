"""Implementation of quick sort algorithm."""
from typing import Sequence


def quick_sort(array: Sequence[int], pivot: int = 0) -> Sequence[int]:
    if len(array) <= 1:
        return array

    pivot = array[pivot]
    if pivot != 0:
        array[pivot], array[0] = array[0], array[pivot]
        pivot = 0
    i, j = 0, 0
    while j < len(array):


    return array
