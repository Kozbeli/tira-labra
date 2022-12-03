import random


def euclidean(a, b):
    """ Etsii suurimman yhteisen tekijän kahdella luvulla käyttäen Euklidean algoritmia.

    Args:
        a (int): ensimmäinen luku
        b (int): toinen luku

    Returns:
        int: suurin yhteinen tekijä
    """

    while a != 0:
        print(f"Calculating euclidean of {a} and {b}")
        temp = a
        a = b % a
        b = temp
    return b


def rabin_miller_primality_test(n, k=128):
    """ Tarkistaa onko luku alkuluku Rabin-Millerin algoritmilla.

    Args:
        n (int): luku
        k (int, optional): testien määrä. Oletuksena 128.

    Returns:
        bool: True jos luku on alkuluku, muuten False
    """

    print(f"\nTesting primality of {n} with {k} rounds of Miller-Rabin\n")
    if n == 2 or n == 3:
        return True
    if n <= 1 or n % 2 == 0:
        return False
    r = 0
    s = n - 1
    while s % 2 == 0:
        r += 1
        s //= 2
    for _ in range(k):
        a = random_between(2, n - 1)
        x = pow(a, s, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True


def random_between(a, b):
    """ Luo satunnaisen luvun väliltä [a, b).

    Args:
        a (int): alaraja
        b (int): yläraja

    Returns:
        int: satunnainen luku
    """

    print(f"\nGenerating random number in range {a} to {b}\n")

    return random.randint(a, b)


def greatest_common_divisor(a, b):
    """ Etsii suurimman yhteisen tekijän kahdella luvulla.

    Args:
        a (int): ensimmäinen luku
        b (int): toinen luku

    Returns:
        int: suurin yhteinen tekijä
    """

    print(f"\nCalculating greatest common divisor of {a} and {b}\n")
    return euclidean(a, b)


def modular_inverse(a, b):
    """ Etsii kahden luvun käänteisluvun.

    Args:
        a (int): ensimmäinen luku
        b (int): toinen luku

    Returns:
        int: käänteisluku
    """
    return pow(a, -1, b)
