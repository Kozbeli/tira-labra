from utils import random_between, rabin_miller_primality_test


def is_prime(n):
    """ Tarkistaa onko luku alkuluku.

    Args:
        n (int): luku
        
    Returns:
        bool: True jos luku on alkuluku, muuten False
    """

    return rabin_miller_primality_test(n)


def generate_prime_number(n):
    """ Luo suuren alkuluvun.

    Args:
        n (int): alkuluvun koko

    Returns:
        int: alkuluku
    """

    print(f"\nGenerating large prime number with {n} bits\n")
    while True:
        p = random_between(pow(2, n - 1), pow(2, n))
        if is_prime(p):
            return p


def generate_prime_pair(n):
    """ Luo suuren alkulukuparin.

    Args:
        n (int): alkulukuparin koko

    Returns:
        tuple: alkulukuparin
    """

    print(f"\nGenerating prime pair with {n} bits\n")
    p = generate_prime_number(n)
    q = generate_prime_number(n)

    while p == q:
        q = generate_prime_number(n)
    return (p, q)
