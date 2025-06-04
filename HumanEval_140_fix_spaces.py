import re

def fix_spaces(text):
    """
    Given a string text, replace all spaces in it with underscores,
    and if a string has more than 2 consecutive spaces,
    then replace all consecutive spaces with -

    fix_spaces("Example") == "Example"
    fix_spaces("Example 1") == "Example_1"
    fix_spaces(" Example 2") == "_Example_2"
    fix_spaces(" Example   3") == "_Example-3"
    """
    # Replace sequences of 3 or more spaces with a hyphen
    text = re.sub(r" {3,}", "-", text)
    # Replace remaining spaces (1 or 2 consecutive) with underscores
    text = text.replace(" ", "_")
    return text
