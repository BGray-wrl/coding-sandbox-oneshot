def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    x_str = str(x)
    num_digits = len(x_str)

    if shift > num_digits:
        return x_str[::-1]
    else:
        effective_shift = shift % num_digits
        return x_str[num_digits - effective_shift:] + x_str[:num_digits - effective_shift]