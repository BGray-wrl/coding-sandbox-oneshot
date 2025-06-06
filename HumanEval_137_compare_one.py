def compare_one(a, b):
    """
    Create a function that takes integers, floats, or strings representing
    real numbers, and returns the larger variable in its given variable type.
    Return None if the values are equal.
    Note: If a real number is represented as a string, the floating point might be . or ,

    compare_one(1, 2.5) ➞ 2.5
    compare_one(1, "2,3") ➞ "2,3"
    compare_one("5,1", "6") ➞ "6"
    compare_one("1", 1) ➞ None
    """
    def _to_float(val):
        if isinstance(val, (int, float)):
            return float(val)
        elif isinstance(val, str):
            return float(val.replace(',', '.'))
        else:
            raise TypeError("Unsupported type for comparison")

    a_float = _to_float(a)
    b_float = _to_float(b)

    if a_float > b_float:
        return a
    elif b_float > a_float:
        return b
    else:
        return None
