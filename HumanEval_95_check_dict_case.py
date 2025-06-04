def check_dict_case(dict):
    """
    Given a dictionary, return True if all keys are strings in lower
    case or all keys are strings in upper case, else return False.
    The function should return False is the given dictionary is empty.
    Examples:
    check_dict_case({"a":"apple", "b":"banana"}) should return True.
    check_dict_case({"a":"apple", "A":"banana", "B":"banana"}) should return False.
    check_dict_case({"a":"apple", 8:"banana", "a":"apple"}) should return False.
    check_dict_case({"Name":"John", "Age":"36", "City":"Houston"}) should return False.
    check_dict_case({"STATE":"NC", "ZIP":"12345" }) should return True.
    """
    if not dict:
        return False

    first_case = None  # 'lower' or 'upper'

    for key in dict.keys():
        if not isinstance(key, str):
            return False

        is_lower = key.islower()
        is_upper = key.isupper()

        if is_lower and not is_upper:  # Truly lowercase
            if first_case is None:
                first_case = 'lower'
            elif first_case == 'upper':
                return False
        elif is_upper and not is_lower:  # Truly uppercase
            if first_case is None:
                first_case = 'upper'
            elif first_case == 'lower':
                return False
        else:
            # This covers:
            # 1. Mixed case strings (e.g., "Name")
            # 2. Strings with no alphabetic characters (e.g., "123", " ")
            # 3. Empty string (e.g., "")
            return False

    return True