from primes import generate_primes, sieve_of_eratosthenes

def main():
  n = 10000
  print(f"generate primes up to {n}")
  primes = generate_primes(n)

  eratothenes_primes = sieve_of_eratosthenes(n)

  for i in range(len(primes)):
    print(f"{primes[i]}, {eratothenes_primes[i]}")

if __name__ == "__main__":
  main()