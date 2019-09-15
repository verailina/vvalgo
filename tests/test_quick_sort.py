"""Tests for quick sort algorithms."""
import pytest

from vvalgo.quick_sort import quick_sort, partition, median_pos, PivotType


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


def test_median():
    """Test the `median` function."""
    assert median_pos(1, 2, 3) == 1
    assert median_pos(3, 2, 3) == 0
    assert median_pos(3, 1, 2) == 2


def test_quick_sort_first():
    """Test quick sort function with first element as a pivot."""
    array = []
    assert quick_sort(array) == 0
    assert array == []

    array = [1]
    assert quick_sort(array) == 0
    assert array == [1]

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


def test_quick_sort_last():
    """Test quick sort function with last element as a pivot."""
    array = []
    assert quick_sort(array, pivot_type=PivotType.Last) == 0
    assert array == []

    array = [1]
    assert quick_sort(array, pivot_type=PivotType.Last) == 0
    assert array == [1]

    array = [2, 1]
    assert quick_sort(array, pivot_type=PivotType.Last) == 1
    assert array == [1, 2]

    array = [3, 1, 2]
    assert quick_sort(array, pivot_type=PivotType.Last) == 2
    assert array == [1, 2, 3]

    array = [2, 7, 3, 1, 5]
    assert quick_sort(array, pivot_type=PivotType.Last) == 7
    assert array == [1, 2, 3, 5, 7]

    array = [5, 2, 3, 4, 1, 1, 1, 1]
    assert quick_sort(array, 1, 4, pivot_type=PivotType.Last) == 6
    assert array == [5, 1, 2, 3, 4, 1, 1, 1]

    array = [1, 2, 3, 4]
    assert quick_sort(array, pivot_type=PivotType.Last) == 6
    assert array == [1, 2, 3, 4]


def test_quick_sort_median():
    """Test quick sort function with median as a pivot."""
    array = []
    assert quick_sort(array, pivot_type=PivotType.Median) == 0
    assert array == []

    array = [1]
    assert quick_sort(array, pivot_type=PivotType.Median) == 0
    assert array == [1]

    array = [2, 1]
    assert quick_sort(array, pivot_type=PivotType.Median) == 1
    assert array == [1, 2]

    array = [3, 1, 2]
    assert quick_sort(array, pivot_type=PivotType.Median) == 2
    assert array == [1, 2, 3]

    array = [2, 7, 3, 1, 5]
    assert quick_sort(array, pivot_type=PivotType.Median) == 6
    assert array == [1, 2, 3, 5, 7]

    array = [5, 2, 3, 4, 1, 1, 1, 1]
    assert quick_sort(array, 1, 4, pivot_type=PivotType.Median) == 4
    assert array == [5, 1, 2, 3, 4, 1, 1, 1]

    array = [1, 2, 3, 4]
    assert quick_sort(array, pivot_type=PivotType.Median) == 4
    assert array == [1, 2, 3, 4]