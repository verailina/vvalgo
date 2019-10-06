"""Implementation of 2SUM problem."""
from typing import Sequence
from collections import Counter


def count_sum_pairs(
        numbers: Sequence[int], lower_bound: int, upper_bound: int) -> int:
    numbers = set(numbers)
    count = 0
    for target in range(lower_bound, upper_bound + 1):
        for x in numbers:
            y = target - x
            if x != y and y in numbers:
                count += 1
                break

    return count
