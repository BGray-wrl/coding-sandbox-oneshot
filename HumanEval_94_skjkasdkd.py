import math

def skjkasdkd(lst):
    """You are given a list of integers.
    You need to find the largest prime value and return the sum of its digits.

    Examples:
    For lst = [0,3,2,1,3,5,7,4,5,5,5,2,181,32,4,32,3,2,32,324,4,3] the output should be 10
    For lst = [1,0,1,8,2,4597,2,1,3,40,1,2,1,2,4,2,5,1] the output should be 25
    For lst = [1,3,1,32,5107,34,83278,109,163,23,2323,32,30,1,9,3] the output should be 13
    For lst = [0,724,32,71,99,32,6,0,5,91,83,0,5,6] the output should be 11
    For lst = [0,81,12,3,1,21] the output should be 3
    For lst = [0,8,1,2,1,7] the output should be 7
    """
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True

    largest_prime = -1
    for num in lst:
        if is_prime(num) and num > largest_prime:
            largest_prime = num

    if largest_prime == -1:
        return 0 # No prime numbers found in the list, or the largest prime was 0 which is not prime.
                 # The problem states "largest prime value", implying at least one prime will be found.
                 # However, if the list contains only non-primes, returning 0 might be an appropriate default.
                 # Based on examples, lists always contain primes.

    sum_of_digits = 0
    for digit in str(largest_prime):
        sum_of_digits += int(digit)
    return sum_of_digits