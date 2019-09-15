"""Tests for quick sort algorithms."""
import pytest

from vvalgo.quick_sort import quick_sort, partition


def test_partition():
    """Test the function `partition`."""
    assert partition([]) == []
    assert partition([1]) == [1]

    with pytest.raises(ValueError, match="invalid array bounds"):
        partition([1, 2], 0, 3)

    assert partition([1, 2, 3]) == [1, 2, 3]
    assert partition([3, 2, 1]) == [1, 2, 3]
    assert partition([3, 2, 1, 0, 4], 0, 2) == [1, 2, 3, 0, 4]
    assert partition([2, 7, 3, 1, 5, 0]) == [0, 1, 2, 7, 5, 3]
