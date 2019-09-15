"""Test for merge sort algorithms."""
import pytest

from vvalgo.merge_sort import (merge, merge_sort, merge_count, SortedArray,
                               merge_sort_count)


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


def test_merge_count():
    """Test merge sort and inversion count algorithm."""
    assert (merge_count(SortedArray([], 0), SortedArray([], 0)) ==
            SortedArray([], 0))
    assert (merge_count(SortedArray([1], 0), SortedArray([2], 0)) ==
            SortedArray([1, 2], 0))
    assert (merge_count(SortedArray([2], 0), SortedArray([1], 0)) ==
            SortedArray([1, 2], 1))
    assert (merge_count(SortedArray([2], 0), SortedArray([0, 1], 1)) ==
            SortedArray([0, 1, 2], 3))
    assert (merge_count(SortedArray([2, 5, 7], 0),
                        SortedArray([1, 3, 4, 6, 8], 0)) ==
            SortedArray([1, 2, 3, 4, 5, 6, 7, 8], 8))

    assert (merge_count(SortedArray([2, 5, 7], 0),
                        SortedArray([1], 0)) ==
            SortedArray([1, 2, 5, 7], 3))

    assert (merge_count(SortedArray([2, 5, 7], 0),
                        SortedArray([1, 4], 0)) ==
            SortedArray([1, 2, 4, 5, 7], 5))


def test_merge_count_with_duplicates():
    """Test the function `merge_sort_count` for the case when the input array
    contains duplicated items.
    """
    assert (merge_count(SortedArray([1, 1], 0), SortedArray([2], 0)) ==
            SortedArray([1, 1, 2], 0))
    assert (merge_count(SortedArray([1, 1], 0), SortedArray([0], 0)) ==
            SortedArray([0, 1, 1], 2))
    assert (merge_count(SortedArray([1, 2], 0), SortedArray([0, 0], 0)) ==
            SortedArray([0, 0, 1, 2], 4))
    assert (merge_count(SortedArray([1, 2], 0), SortedArray([3, 3], 0)) ==
            SortedArray([1, 2, 3, 3], 0))
    assert (merge_count(SortedArray([1, 3], 0), SortedArray([2, 2], 0)) ==
            SortedArray([1, 2, 2, 3], 2))
    assert (merge_count(SortedArray([1, 1, 3, 3], 0),
                        SortedArray([2, 2, 5, 5], 0)) ==
            SortedArray([1, 1, 2, 2, 3, 3, 5, 5], 4))
    assert (merge_count(SortedArray([1, 2, 3], 0),
                        SortedArray([0, 1, 2], 0)) ==
            SortedArray([0, 1, 1, 2, 2, 3], 6))

    assert (merge_count(SortedArray([1, 2, 2], 0),
                        SortedArray([2, 3], 0)) ==
            SortedArray([1, 2, 2, 2, 3], 0))


def test_merge_sort_count():
    """Test `merge_sort_count` function."""
    assert merge_sort_count([]) == SortedArray([], 0)
    assert merge_sort_count([1]) == SortedArray([1], 0)
    assert merge_sort_count([1, 0]) == SortedArray([0, 1], 1)
    assert merge_sort_count([5, 1, 2]) == SortedArray([1, 2, 5], 2)
    assert merge_sort_count([5, 1, 3, 2]) == SortedArray([1, 2, 3, 5], 4)
    assert merge_sort_count([1, 2, 3, 4]) == SortedArray([1, 2, 3, 4], 0)
    assert merge_sort_count([1, 3, 2, 5, 4, 0]) == SortedArray(
        [0, 1, 2, 3, 4, 5], 7)
    assert (merge_sort_count([37, 7, 2, 14, 35, 47, 10, 24, 44, 17, 34, 11, 16,
                              48, 1, 39, 6, 33, 43, 26, 40, 4, 28, 5, 38, 41, 42,
                              12, 13, 21, 29, 18, 3, 19, 0, 32, 46, 27, 31, 25,
                              15, 36, 20, 8, 9, 49, 22, 23, 30, 45]
                             ).n_inversions == 590)


def test_merge_sort_count_with_duplicates():
    """Test the function `merge_sort_count` in the case when the input array
    contains duplicated items.
    """
    assert merge_sort_count([1, 1]) == SortedArray([1, 1], 0)
    assert merge_sort_count([1, 2, 1]) == SortedArray([1, 1, 2], 1)
    assert merge_sort_count([1, 5, 2, 3, 5, 6]) == SortedArray(
        [1, 2, 3, 5, 5, 6], 2)
    assert merge_sort_count([5, 1, 2, 3, 5]) == SortedArray(
        [1, 2, 3, 5, 5], 3)


def test_merge_sort_count_big(resources_path):
    """Test the function `merge_sort_count` on a big example."""
    with (resources_path / "merge_count_sample.txt").open("r") as input_file:
        array = [int(line) for line in input_file.readlines()]
        assert merge_sort_count(array).n_inversions == 2407905288
