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
        temp = a
        a = b % a
        b = temp
    return b


def sieve_of_eratosthenes(number=1000):
    """ Luo suuren alkulukulistan. Aikavaativuus O(n log log n).

    Args:
        number (int): luku

    Returns:
        list: alkulukulista
    """

    primes = []
    is_prime = [True] * (number + 1)
    is_prime[0] = is_prime[1] = False

    for i in range(2, number + 1):
        if is_prime[i]:
            primes.append(i)
            for j in range(i * i, number + 1, i):
                is_prime[j] = False

    return primes


def rabin_miller_primality_test(n, k=40):
    """ Tarkistaa onko luku alkuluku Rabin-Millerin algoritmilla. Aikavaativuus O(k log^3 n).

    Args:
        n (int): luku
        k (int, optional): testien määrä. Oletuksena 40.

    Returns:
        bool: True jos luku on alkuluku, muuten False
    """

    # Luvut 2 ja 3 ovat alkulukuja
    if n == 2 or n == 3:
        return True

    # Parilliset tai ykkösestä pienemmät luvut eivät ole alkulukuja
    if n <= 1 or n % 2 == 0:
        return False

    r = 0
    s = n - 1

    # Selvitetään suurin kahden potenssi, joka jakaa luvun n - 1
    while s % 2 == 0:
        r += 1
        s //= 2

    # Todenäköisyys, että luku on alkuluku on 1 - 1/4^k
    for _ in range(k):

        # Arvotaan satunnainen luku väliltä [2, n - 1]
        a = random_between(2, n - 1)

        # Lasketaan a^s mod n
        x = pow(a, s, n)

        # Jos x = 1 tai x = n - 1, luku on todennäköisesti alkuluku
        if x == 1 or x == n - 1:
            continue

        # Jos x != 1 ja x != n - 1 , testataan seuraavat 2^r - 1 kertaa
        for _ in range(r - 1):

            # Lasketaan x^2 mod n
            x = pow(x, 2, n)

            # Jos x = n - 1, luku on todennäköisesti alkuluku
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

    return random.randint(a, b)


def greatest_common_factor(a, b):
    """ Etsii suurimman yhteisen tekijän kahdella luvulla.

    Args:
        a (int): ensimmäinen luku
        b (int): toinen luku

    Returns:
        int: suurin yhteinen tekijä
    """

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
