def is_nested(string):
    """
    Create a function that takes a string as input which contains only square brackets.
    The function should return True if and only if there is a valid subsequence of brackets 
    where at least one bracket in the subsequence is nested.

    is_nested('[[]]') ➞ True
    is_nested('[]]]]]]][[[[[]') ➞ False
    is_nested('[][]') ➞ False
    is_nested('[]') ➞ False
    is_nested('[[][]]') ➞ True
    is_nested('[[]][[') ➞ True
    """
    open_count = 0
    found_nested_subsequence = False

    for char in string:
        if char == '[':
            open_count += 1
        elif char == ']':
            # If we are closing a bracket and there were at least two open brackets
            # before this one, it means this is a nested bracket.
            if open_count >= 2:
                found_nested_subsequence = True
            open_count -= 1
            # It's possible for open_count to go negative if there are unmatched closing brackets.
            # However, this doesn't invalidate `found_nested_subsequence` if it was already True,
            # as we are looking for *any* valid nested subsequence.
    return found_nested_subsequence