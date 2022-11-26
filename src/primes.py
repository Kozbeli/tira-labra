import random


def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def generate_primes(n):
    primes = []
    for i in range(2, n + 1):
        if is_prime(i):
            primes.append(i)
    return primes


def sieve_of_eratosthenes(n):
    primes = []
    for i in range(2, n + 1):
        primes.append(i)
    for i in range(2, n + 1):
        if i in primes:
            for j in range(i * 2, n + 1, i):
                if j in primes:
                    primes.remove(j)
    return primes


def random_range(a, b):
    print(f"\nGenerating random number in range {a} to {b}\n")
    return random.randint(a, b)


def miller_rabin_primality_test(n, k):
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
        a = random_range(2, n - 1)
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


def random_bits(bits):
    return random.getrandbits(bits)


def generate_prime_number(bits):
    print(f"\nGenerating prime number with {bits} bits\n")
    while True:
        n = random_bits(bits)
        if miller_rabin_primality_test(n, 128):
            return n
