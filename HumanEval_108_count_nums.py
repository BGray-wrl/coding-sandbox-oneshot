def count_nums(arr):
    """
    Write a function count_nums which takes an array of integers and returns
    the number of elements which has a sum of digits > 0.
    If a number is negative, then its first signed digit will be negative:
    e.g. -123 has signed digits -1, 2, and 3.
    >>> count_nums([]) == 0
    >>> count_nums([-1, 11, -11]) == 1
    >>> count_nums([1, 1, 2]) == 3
    """
    count = 0
    for num in arr:
        s_num = str(num)
        sum_digits = 0
        if num < 0:
            sum_digits += -int(s_num[1])
            for digit_char in s_num[2:]:
                sum_digits += int(digit_char)
        else:
            for digit_char in s_num:
                sum_digits += int(digit_char)
        
        if sum_digits > 0:
            count += 1
    return count