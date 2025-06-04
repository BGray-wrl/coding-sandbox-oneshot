def anti_shuffle(s):
    """
    Write a function that takes a string and returns an ordered version of it.
    Ordered version of string, is a string where all words (separated by space)
    are replaced by a new word where all the characters arranged in
    ascending order based on ascii value.
    Note: You should keep the order of words and blank spaces in the sentence.

    For example:
    anti_shuffle('Hi') returns 'Hi'
    anti_shuffle('hello') returns 'ehllo'
    anti_shuffle('Hello World!!!') returns 'Hello !!!Wdlor'
    """
    result_parts = []
    current_word = []
    current_spaces = []

    for char in s:
        if char == ' ':
            if current_word:
                result_parts.append("".join(sorted(current_word)))
                current_word = []
            current_spaces.append(char)
        else:
            if current_spaces:
                result_parts.append("".join(current_spaces))
                current_spaces = []
            current_word.append(char)

    if current_word:
        result_parts.append("".join(sorted(current_word)))
    if current_spaces:
        result_parts.append("".join(current_spaces))

    return "".join(result_parts)