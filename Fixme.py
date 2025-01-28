def triangular(n):
    '''
    Returns the nth triangular number.

    The nth triangular number is the sum of all numbers from 1 to n.
    It is like the factorial, but uses addition instead of multiplication.

    >>> triangular(1)
    1
    >>> triangular(2)
    3
    >>> triangular(3)
    6
    >>> triangular(4)
    10
    >>> triangular(40)
    820
    >>> triangular(400)
    80200
    '''
    result = 0
    for i in range(1, n + 1):
        result += i
    return result
