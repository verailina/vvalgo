from vvalgo.long_arithmetic import (karatsuba_multiply,
                                    multiply_by_integer,
                                    add, compare, sub,
                                    multiply_by_ten)

import pytest


def test_multiply_by_integer():
    assert multiply_by_integer([1, 2, 3, 4], 1) == [1, 2, 3, 4]
    assert multiply_by_integer([1, 2, 3, 4], 2) == [2, 4, 6, 8]
    assert multiply_by_integer([1, 2, 3, 4], 0) == [0]
    assert multiply_by_integer([1, 2, 3, 4], 5) == [6, 1, 7, 0]
    assert multiply_by_integer([1, 2, 3, 4], 9) == [1, 1, 1, 0, 6]


def test_add():
    assert add([1], [0]) == [1]
    assert add([1], [9]) == [1, 0]
    assert add([1], [1, 1]) == [1, 2]
    assert add([9], [1, 2]) == [2, 1]
    assert add([9], [9, 2]) == [1, 0, 1]


def test_compare():
    assert compare([1], [0])
    assert not compare([0], [1])
    assert compare([1, 1, 0], [1, 0])
    assert compare([1, 0], [1, 0])
    assert not compare([1, 0], [1, 1, 0])


def test_sub():
    res = sub([1], [0])
    assert not res[0]
    assert res[1] == [1]

    res = sub([0], [1])
    assert res[0]
    assert res[1] == [1]

    res = sub([1], [1])
    assert not res[0]
    assert res[1] == [0]

    res = sub([1, 0], [1])
    assert not res[0]
    assert res[1] == [9]

    res = sub([1], [1, 0])
    assert res[0]
    assert res[1] == [9]

    res = sub([1, 0, 0, 0], [1, 1])
    assert not res[0]
    assert res[1] == [9, 8, 9]

    res = sub([1, 9, 0], [8, 6])
    assert not res[0]
    assert res[1] == [1, 0, 4]


def test_multiply_by_ten():
    with pytest.raises(ValueError, match="invalid ten_pow"):
        multiply_by_ten([1], -1)

    assert multiply_by_ten([1, 1], 0) == [1, 1]
    assert multiply_by_ten([1], 1) == [1, 0]
    assert multiply_by_ten([1, 0, 0], 2) == [1, 0, 0, 0, 0]


def test_karatsuba_multiply():
    with pytest.raises(ValueError, match="invalid input"):
        karatsuba_multiply([], [1])

    assert karatsuba_multiply([1], [1]) == [1]
    assert karatsuba_multiply([1, 1], [2]) == [2, 2]
    assert karatsuba_multiply([3], [2, 4]) == [7, 2]

    assert karatsuba_multiply([1, 2], [1, 0]) == [1, 2, 0]
    assert karatsuba_multiply([1, 0], [1, 2]) == [1, 2, 0]
    assert karatsuba_multiply([1, 2], [1, 2, 1]) == [1, 4, 5, 2]
    assert karatsuba_multiply([1, 2, 1], [1, 2, 1]) == [1, 4, 6, 4, 1]
    assert karatsuba_multiply([1, 1, 1], [1, 1]) == [1, 2, 2, 1]
    assert karatsuba_multiply([1, 1], [8, 6, 9]) == [9, 5, 5, 9]
    assert karatsuba_multiply([1, 0], [1, 0, 1, 0, 9]) == [1, 0, 1, 0, 9, 0]
    assert karatsuba_multiply([2, 1], [9, 6, 0]) == [2, 0, 1, 6, 0]


def test_karatsuba_multiply_stress():
    for _first in range(1, 10**3):
        for second in range(1, 10**3):
            first = int(_first)
            expected = first * second
            first = [int(d) for d in str(first)]
            second = [int(d) for d in str(second)]
            actual = karatsuba_multiply(first, second)
            actual = int("".join(str(d) for d in actual))
            assert actual == expected


def test_karatsuba_multiply_long():
    x = "3141592653589793238462643383279502884197169399375105820974944592"
    y = "2718281828459045235360287471352662497757247093699959574966967627"
    expected_result = int(x) * int(y)
    x = [int(d) for d in x]
    y = [int(d) for d in y]
    res = karatsuba_multiply(x, y)
    res = int("".join([str(d) for d in res]))
    assert res == expected_result
