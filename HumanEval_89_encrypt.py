def encrypt(s):
    """Create a function encrypt that takes a string as an argument and
    returns a string encrypted with the alphabet being rotated. 
    The alphabet should be rotated in a manner such that the letters 
    shift down by two multiplied to two places.
    For example:
    encrypt('hi') returns 'lm'
    encrypt('asdfghjkl') returns 'ewhjklnop'
    encrypt('gf') returns 'kj'
    encrypt('et') returns 'ix'
    """
    encrypted_chars = []
    for char in s:
        if 'a' <= char <= 'z':
            # Calculate the shifted character's ASCII value
            # 'a' is ASCII 97. Shift by 4.
            shifted_char_code = ord(char) + 4
            
            # Handle wrap-around for letters beyond 'z'
            if shifted_char_code > ord('z'):
                shifted_char_code = ord('a') + (shifted_char_code - ord('z') - 1)
            encrypted_chars.append(chr(shifted_char_code))
        else:
            encrypted_chars.append(char)
    return "".join(encrypted_chars)