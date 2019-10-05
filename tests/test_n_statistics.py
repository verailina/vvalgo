from vvalgo.n_statistics import InteractiveMedian


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
