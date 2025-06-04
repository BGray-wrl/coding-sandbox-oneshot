import math


def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[1] * x^2 + .... xs[n] * x^n
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])


def find_zero(xs: list):
    """ xs are coefficients of a polynomial.
    find_zero find x such that poly(x) = 0.
    find_zero returns only only zero point, even if there are many.
    Moreover, find_zero only takes list xs having even number of coefficients
    and largest non zero coefficient as it guarantees
    a solution.
    >>> round(find_zero([1, 2]), 2) # f(x) = 1 + 2x
    -0.5
    >>> round(find_zero([-6, 11, -6, 1]), 2) # (x - 1) * (x - 2) * (x - 3) = -6 + 11x - 6x^2 + x^3
    1.0
    """
    low = -1000.0
    high = 1000.0
    tolerance = 1e-7
    max_iterations = 100

    for _ in range(max_iterations):
        mid = (low + high) / 2
        f_mid = poly(xs, mid)

        if abs(f_mid) < tolerance:
            return mid

        f_low = poly(xs, low)
        
        # If f_low and f_mid have opposite signs, root is in [low, mid]
        if f_low * f_mid < 0:
            high = mid
        # Otherwise, root is in [mid, high]
        else:
            low = mid
            
    # After max_iterations, mid is the approximate root
    return (low + high) / 2