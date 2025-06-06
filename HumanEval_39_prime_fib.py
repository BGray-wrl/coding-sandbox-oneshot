def prime_fib(n: int):
    """
    prime_fib returns n-th number that is a Fibonacci number and it's also prime.
    >>> prime_fib(1)
    2
    >>> prime_fib(2)
    3
    >>> prime_fib(3)
    5
    >>> prime_fib(4)
    13
    >>> prime_fib(5)
    89
    """
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    prime_fib_numbers = []
    a, b = 0, 1
    while len(prime_fib_numbers) < n:
        next_fib = a + b
        a = b
        b = next_fib
        if is_prime(next_fib):
            prime_fib_numbers.append(next_fib)
    return prime_fib_numbers[n - 1]