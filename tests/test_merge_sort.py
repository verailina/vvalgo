"""Test for merge sort algorithms."""
from vvalgo.merge_sort import merge, merge_sort


def test_merge():
    """Test merge of two sorted arrays."""
    assert merge([], []) == []
    assert merge([1], []) == [1]
    assert merge([], [1]) == [1]
    assert merge([1], [2]) == [1, 2]
    assert merge([2], [1, 1]) == [1, 1, 2]
    assert (merge([1, 1, 2, 3, 4], [2, 3, 3, 3, 5, 6, 7, 8]) ==
            [1, 1, 2, 2, 3, 3, 3, 3, 4, 5, 6, 7, 8])


def test_merge_sort():
    """Test merge sort algorithm."""
    assert merge_sort([]) == []
    assert merge_sort([1]) == [1]
    assert merge_sort([1, 2]) == [1, 2]
    assert merge_sort([2, 1]) == [1, 2]
    assert merge_sort([4, 3, 2, 1, 0]) == [0, 1, 2, 3, 4]
    assert merge_sort([1, 2, 1, 2, 3, -1]) == [-1, 1, 1, 2, 2, 3]