def check_if_last_char_is_a_letter(txt):
    """
    Create a function that returns True if the last character
    of a given string is an alphabetical character and is not
    a part of a word, and False otherwise.
    Note: "word" is a group of characters separated by space.

    Examples:
    check_if_last_char_is_a_letter("apple pie") ➞ False
    check_if_last_char_is_a_letter("apple pi e") ➞ True
    check_if_last_char_is_a_letter("apple pi e ") ➞ False
    check_if_last_char_is_a_letter("") ➞ False 
    """
    if not txt:
        return False
    
    last_char = txt[-1]
    
    if not last_char.isalpha():
        return False
    
    # If the string has only one character and it's a letter, it's considered not part of a word
    if len(txt) == 1:
        return True
    
    # If the string has more than one character, the character before the last one must be a space
    # for the last character to be considered "not a part of a word".
    return txt[-2] == ' '
