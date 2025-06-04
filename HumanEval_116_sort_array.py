def sort_array(arr):
    """
    In this Kata, you have to sort an array of non-negative integers according to
    number of ones in their binary representation in ascending order.
    For similar number of ones, sort based on decimal value.

    It must be implemented like this:
    >>> sort_array([1, 5, 2, 3, 4]) == [1, 2, 3, 4, 5]
    >>> sort_array([-2, -3, -4, -5, -6]) == [-6, -5, -4, -3, -2]
    >>> sort_array([1, 0, 2, 3, 4]) [0, 1, 2, 3, 4]
    """
    def custom_key(n):
        if n < 0:
            # For negative numbers, sort purely by their decimal value.
            # Using -1 as the first element ensures they come before any non-negative numbers
            # (as non-negative numbers will have a bit count >= 0 for the first element).
            return (-1, n)
        else:
            # For non-negative numbers:
            # Primary sort: count of '1's in binary representation.
            # Secondary sort: decimal value.
            return (bin(n).count('1'), n)

    return sorted(arr, key=custom_key)