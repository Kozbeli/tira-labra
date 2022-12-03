import unittest
from primegenerator import generate_prime_pair, generate_prime_number, is_prime


class TestPrimeGenerator(unittest.TestCase):

    def test_is_prime(self):
        self.assertEqual(is_prime(7), True)

    def test_generate_prime_number(self):
        prime = generate_prime_number(10)
        self.assertEqual(is_prime(prime), True)

    def test_generate_prime_pair(self):
        pair = generate_prime_pair(10)
        self.assertEqual(is_prime(pair[0]), True)
        self.assertEqual(is_prime(pair[1]), True)
        self.assertNotEqual(pair[0], pair[1])
