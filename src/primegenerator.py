from utils import random_between, rabin_miller_primality_test, sieve_of_eratosthenes


def is_prime(number):
    """ Tarkistaa onko luku alkuluku.

    Args:
        n (int): luku

    Returns:
        bool: True jos luku on alkuluku, muuten False
    """

    primes = sieve_of_eratosthenes()

    if number in primes:
        return True

    for prime in primes:
        if number % prime == 0:
            return False

    return rabin_miller_primality_test(number)


def generate_prime_number(n):
    """ Luo suuren alkuluvun.

    Args:
        n (int): alkuluvun koko

    Returns:
        int: alkuluku
    """

    while True:
        prime = random_between(pow(2, n - 1), pow(2, n))
        if is_prime(prime):
            return prime


def generate_prime_pair(n):
    """ Luo suuren alkulukuparin.

    Args:
        n (int): alkulukuparin koko

    Returns:
        tuple: alkulukupari
    """

    # print(f"\nGenerating prime pair with {n} bits\n")
    p = generate_prime_number(n)
    q = generate_prime_number(n)

    while p == q:
        q = generate_prime_number(n)
    return (p, q)
