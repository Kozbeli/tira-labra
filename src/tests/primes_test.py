import unittest
from primes import is_prime, generate_primes, sieve_of_eratosthenes

class TestPrimes(unittest.TestCase):

  def test_is_five_prime(self):
    self.assertTrue(is_prime(5))

  def test_is_four_prime(self): 
    self.assertFalse(is_prime(4))

  def test_generate_primes(self):
    self.assertEqual(generate_primes(10), [2, 3, 5, 7])

  def test_generate_primes_by_sieve_of_eratosthenes(self):
    self.assertEqual(sieve_of_eratosthenes(10), [2, 3, 5, 7])

