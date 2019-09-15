"""Tests for quick sort algorithms."""
import pytest

from vvalgo.quick_sort import quick_sort, partition


def test_partition():
    """Test the function `partition`."""
    array = []
    assert partition([]) == 0
    assert array == []
    array = [1]
    assert partition([1]) == 0
    assert array == [1]

    with pytest.raises(ValueError, match="invalid array bounds"):
        partition([1, 2], 0, 3)

    array = [1, 2, 3]
    assert partition(array) == 0
    assert array == [1, 2, 3]
    array = [3, 2, 1]
    assert partition(array) == 2
    assert array == [1, 2, 3]
    array = [3, 2, 1, 0, 4]
    assert partition(array, 0, 2) == 2
    assert array == [1, 2, 3, 0, 4]
    array = [2, 7, 3, 1, 5, 0]
    assert partition(array) == 2
    assert array == [0, 1, 2, 7, 5, 3]


def test_quick_sort():
    """Test quick sort function."""
    array = []
    assert quick_sort(array) == 0
    assert array == []

    array = [1]
    n_comparisons = 0
    assert quick_sort(array) == 0
    assert array == [1]
    assert n_comparisons == 0

    array = [2, 1]
    assert quick_sort(array) == 1
    assert array == [1, 2]

    array = [3, 1, 2]
    assert quick_sort(array) == 3
    assert array == [1, 2, 3]

    array = [2, 7, 3, 1, 5]
    assert quick_sort(array) == 7
    assert array == [1, 2, 3, 5, 7]

    array = [5, 2, 3, 4, 1, 1, 1, 1]
    assert quick_sort(array, 1, 4) == 4
    assert array == [5, 1, 2, 3, 4, 1, 1, 1]

    array = [1, 2, 3, 4]
    assert quick_sort(array) == 6
    assert array == [1, 2, 3, 4]
