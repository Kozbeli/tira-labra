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


def rabin_miller_primality_test(n, k = 128):
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


def low_primes():
  return [
    2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 
    47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 
    107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 
    167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 
    229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 
    283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 
    359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 
    431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 
    491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 
    571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 
    641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 
    709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 
    787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 
    859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 
    941, 947, 953, 967, 971, 977, 983, 991, 997
    ]


def is_prime(n):
  print(f"\nChecking if {n} is prime\n")

  if n < 2:
    return False
  if n in low_primes():
    return True
  for prime in low_primes():
    if n % prime == 0:
      return False
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
  
  
