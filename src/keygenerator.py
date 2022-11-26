import random


def modular_inverse(a, b):
    return pow(a, -1, b)


def euclidean(a, b):
    while a != 0:
        print(f"Calculating euclidean of {a} and {b}")
        temp = a
        a = b % a
        b = temp
    return b


def greatest_common_divisor(a, b):
    print(f"\nCalculating greatest common divisor of {a} and {b}\n")
    return euclidean(a, b)


def rabin_miller_primality_test(n, k=128):
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


def is_prime(n):
    return rabin_miller_primality_test(n)


def random_between(a, b):
    print(f"\nGenerating random number in range {a} to {b}\n")

    return random.randint(a, b)


def generate_prime_number(n):
    print(f"\nGenerating large prime number with {n} bits\n")
    while True:
        p = random_between(pow(2, n - 1), pow(2, n))
        if is_prime(p):
            return p


def generate_prime_pair(n):
    print(f"\nGenerating prime pair with {n} bits\n")
    p = generate_prime_number(n)
    q = generate_prime_number(n)

    while p == q:
        q = generate_prime_number(n)
    return (p, q)


def generate_key_pair(key_size):
    print(f"\nGenerating key pair with {key_size} bits\n")
    (p, q) = generate_prime_pair(key_size)
    print(f"\nGenerated prime pair: {p}, {q}\n")
    n = p * q

    while True:
        e = random_between(pow(2, key_size - 1), pow(2, key_size))
        print(f"\nGenerated random number: {e}\n")
        if greatest_common_divisor(e, (p - 1) * (q - 1)) == 1:
            break

    d = modular_inverse(e, (p - 1) * (q - 1))
    public_key = (n, e)
    private_key = (n, d)
    return (public_key, private_key)
