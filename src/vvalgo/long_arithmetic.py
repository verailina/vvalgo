"""This module implements long arithmetic algorithms for adding, subtracting
and multiplying long integers. For multiplication, the Karatsuba algorithm is
used.
"""
from typing import Sequence, Tuple


def multiply_by_integer(x: Sequence[int], const: int) -> Sequence[int]:
    """Multiply by constant."""
    if const == 0:
        return [0]
    i = len(x) - 1
    result = [0 for _ in range(len(x) + 1)]
    carry = 0
    while i >= 0:
        mult = x[i] * const + carry
        result[i + 1] = mult % 10
        carry = mult // 10
        i -= 1
    if carry > 0:
        result[0] = carry
    else:
        result = result[1:]
    return result


def add(x: Sequence[int], y: Sequence[int]) -> Sequence[int]:
    """Sum two long integers."""
    base, to_add = ([0] + x, y) if len(x) > len(y) else ([0] + y, x)
    i = 1
    carry = 0
    while i <= len(base):
        base[-i] += carry
        if i <= len(to_add):
            base[-i] += to_add[-i]
        carry = base[-i] // 10
        base[-i] %= 10
        i += 1

    if base[0] == 0:
        base = base[1:]
    return base


def compare(x: Sequence[int], y: Sequence[int]) -> bool:
    """Check whether first number is greater than or equal to the second one."""
    if len(x) > len(y):
        return True
    if len(y) > len(x):
        return False
    i = 0
    while i < len(x):
        if x[i] > y[i]:
            return True
        if y[i] > x[i]:
            return False
        i += 1
    return True


def sub(x: Sequence[int], y: Sequence[int]) -> Tuple[bool, Sequence[int]]:
    """Subtraction for long integers."""
    sign = False
    if not compare(x, y):
        sign = True
        x, y = y, x
    i = 1
    res = [d for d in x]
    carry = 0
    while i <= len(x):
        res[-i] -= carry
        carry = 0
        if i <= len(y):
            res[-i] -= y[-i]
        if res[-i] < 0:
            res[-i] += 10
            carry = 1
        i += 1
    start = 0
    while start < len(res) - 1 and res[start] == 0:
        start += 1

    return sign, res[start:]


def multiply_by_ten(x: Sequence[int], ten_pow: int) -> Sequence[int]:
    """Multiply number by power of 10."""
    if ten_pow < 0:
        raise ValueError(f"invalid ten_pow: {ten_pow}, can not be negative.")
    return x + [0 for _ in range(ten_pow)]


def karatsuba_multiply(x: Sequence[int], y: Sequence[int]) -> Sequence[int]:
    if len(x) == 0 or len(y) == 0:
        raise ValueError(f"invalid input, numbers can't be empty: x={x}, y={y}")
    if len(x) == 1:
        return multiply_by_integer(y, x[0])
    if len(y) == 1:
        return multiply_by_integer(x, y[0])

    x_mid = len(x) // 2
    y_mid = len(y) // 2
    a = x[:-x_mid]
    b = x[-x_mid:]
    c = y[:-y_mid]
    d = y[-y_mid:]
    a_c = karatsuba_multiply(a, c)
    b_d = karatsuba_multiply(b, d)
    z = karatsuba_multiply(add(a, b), add(c, d))
    z = sub(z, a_c)[1]
    z = sub(z, b_d)[1]
    a_c_10 = multiply_by_ten(a_c, len(b) + len(d))
    z_10 = multiply_by_ten(z, min(len(b), len(d)))
    res = add(a_c_10, b_d)
    res = add(res, z_10)

    return res
