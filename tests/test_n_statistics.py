import pytest

from vvalgo.n_statistics import InteractiveMedian, find_n_statistics


def test_interactive_median():
    """Test the method `insert` of the class `InteractiveMedian`."""
    solver = InteractiveMedian(10)
    assert solver.insert(1) == 1
    assert solver.medan_sum == 1

    assert solver.insert(5) == 1
    assert solver.medan_sum == 2

    assert solver.insert(3) == 3
    assert solver.medan_sum == 5

    assert solver.insert(1) == 1
    assert solver.medan_sum == 6

    assert solver.insert(2) == 2
    assert solver.medan_sum == 8

    assert solver.insert(2) == 2
    assert solver.medan_sum == 0


def test_big_sample(resources_path):
    solver = InteractiveMedian()
    with (resources_path / "median_sample.txt").open("r") as input_file:
        for line in input_file.readlines():
            solver.insert(int(line))

    print(solver.medan_sum)


def test_find_n_statistics():
    """Test the function that finds an n-th statistics of an input array."""
    with pytest.raises(ValueError, match="invalid n"):
        find_n_statistics([], 1)

    assert find_n_statistics([1], 1) == 1

    assert find_n_statistics([1, 2], 1) == 1
    assert find_n_statistics([2, 1], 2) == 2

    assert find_n_statistics([2, 1, 3], 1) == 1
    assert find_n_statistics([2, 1, 3], 2) == 2
    assert find_n_statistics([2, 1, 3], 3) == 3

    assert find_n_statistics([2, 3, 1, 3], 1) == 1
    assert find_n_statistics([2, 3, 1, 3], 2) == 2
    assert find_n_statistics([2, 3, 1, 3], 3) == 3
    assert find_n_statistics([2, 3, 1, 3], 4) == 3
