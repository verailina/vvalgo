"""Test for merge sort algorithms."""
from vvalgo.merge_sort import merge


def test_merge():
    """Test merge of two sorted arrays."""
    assert merge([], []) == []
    assert merge([1], []) == [1]
    assert merge([], [1]) == [1]
    assert merge([1], [2]) == [1, 2]
    assert merge([2], [1, 1]) == [1, 1, 2]
    assert (merge([1, 1, 2, 3, 4], [2, 3, 3, 3, 5, 6, 7, 8]) ==
            [1, 1, 2, 2, 3, 3, 3, 3, 4, 5, 6, 7, 8])