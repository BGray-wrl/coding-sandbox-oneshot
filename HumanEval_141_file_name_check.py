def file_name_check(file_name):
    """Create a function which takes a string representing a file's name, and returns
    'Yes' if the the file's name is valid, and returns 'No' otherwise.
    A file's name is considered to be valid if and only if all the following conditions 
    are met:
    - There should not be more than three digits ('0'-'9') in the file's name.
    - The file's name contains exactly one dot '.'
    - The substring before the dot should not be empty, and it starts with a letter from 
    the latin alphapet ('a'-'z' and 'A'-'Z').
    - The substring after the dot should be one of these: ['txt', 'exe', 'dll']
    Examples:
    file_name_check("example.txt") # => 'Yes'
    file_name_check("1example.dll") # => 'No' (the name should start with a latin alphapet letter)
    """
    # Condition 1: No more than three digits
    digit_count = sum(c.isdigit() for c in file_name)
    if digit_count > 3:
        return 'No'

    # Condition 2: Exactly one dot
    parts = file_name.split('.')
    if len(parts) != 2:
        return 'No'

    before_dot, after_dot = parts[0], parts[1]

    # Condition 3: The substring before the dot
    # - Should not be empty
    if not before_dot:
        return 'No'
    # - Starts with a letter from the latin alphabet
    if not before_dot[0].isalpha():
        return 'No'

    # Condition 4: The substring after the dot
    valid_extensions = ['txt', 'exe', 'dll']
    if after_dot not in valid_extensions:
        return 'No'

    return 'Yes