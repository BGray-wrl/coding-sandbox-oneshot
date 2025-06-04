def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    if n == 1:
        return 1
    else:
        # Numbers starting with 1: 1 * 10^(n-1)
        # Numbers ending with 1: 9 * 10^(n-2) (first digit can't be 0)
        # Numbers starting AND ending with 1: 1 * 10^(n-2)
        
        # Using Principle of Inclusion-Exclusion:
        # Count = (Starts with 1) + (Ends with 1) - (Starts AND Ends with 1)
        return (10**(n - 1)) + (9 * (10**(n - 2))) - (10**(n - 2))