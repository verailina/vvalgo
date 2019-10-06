from vvalgo.two_sum import count_sum_pairs


def test_count_sum_pairs():
    """Test the function `count_two_pairs`."""
    assert count_sum_pairs([], 0, 0) == 0
    assert count_sum_pairs([1, 2], 1, 1) == 0
    assert count_sum_pairs([1, 1], 1, 2) == 0
    assert count_sum_pairs([1, 1], 1, 1) == 0
    assert count_sum_pairs([0, 2], 1, 2) == 1
    assert count_sum_pairs([1, 1, 2], 1, 3) == 1
    assert count_sum_pairs([0, 1, 2], 1, 3) == 3


def test_count_sum_paris_big(resources_path):
    """Test the function `merge_sort_count` on a big example."""
    with (resources_path / "sum_sample.txt").open("r") as input_file:
        array = [int(line) for line in input_file.readlines()]
        print(count_sum_pairs(array, -10**4, 10**4))
