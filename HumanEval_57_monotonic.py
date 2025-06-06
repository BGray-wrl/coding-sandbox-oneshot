def monotonic(l: list):
    """Return True is list elements are monotonically increasing or decreasing.
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    """
    if len(l) <= 1:
        return True

    is_increasing = True
    is_decreasing = True

    for i in range(1, len(l)):
        if l[i] > l[i-1]:
            is_decreasing = False
        elif l[i] < l[i-1]:
            is_increasing = False
    
    return is_increasing or is_decreasing