

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