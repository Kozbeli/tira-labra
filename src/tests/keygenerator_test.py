import unittest
from keygenerator import modular_inverse, euclidean, greatest_common_divisor, rabin_miller_primality_test, is_prime, random_between, generate_prime_number, generate_prime_pair, generate_key_pair


class TestKeyGeneratot(unittest.TestCase):
    def setUp(self):
        self.large_prime_one = 7085941877374168726938565836561948189008651469398676362247735437505254012699743365086256920443683047
        self.large_prime_two = 2257883104325493496507757132367951174929467670065779796681817783787048988554904746782055125469000289
        self.composite = self.large_prime_one * self.large_prime_two

    def test_modular_inverse(self):
        self.assertEqual(modular_inverse(7, 40), 23)

    def test_euclidean(self):
        self.assertEqual(euclidean(252, 105), 21)

    def test_greatest_common_divisor(self):
        self.assertEqual(greatest_common_divisor(252, 105), 21)

    def test_rabin_miller_primality_with_small_primes(self):
        self.assertEqual(rabin_miller_primality_test(2), True)
        self.assertEqual(rabin_miller_primality_test(3), True)
        self.assertEqual(rabin_miller_primality_test(7), True)

    def test_rabin_miller_primality_with_large_prime(self):
        self.assertEqual(rabin_miller_primality_test(
            self.large_prime_one), True)
        self.assertEqual(rabin_miller_primality_test(
            self.large_prime_two), True)

    def test_rabin_miller_primality__with_composite(self):
        self.assertEqual(rabin_miller_primality_test(self.composite), False)

    def test_is_prime(self):
        self.assertEqual(is_prime(7), True)

    def test_random_between(self):
        random = random_between(1, 10)
        self.assertGreater(random, 1)
        self.assertLessEqual(random, 10)

    def test_generate_prime_number(self):
        prime = generate_prime_number(10)
        self.assertEqual(is_prime(prime), True)

    def test_generate_prime_pair(self):
        pair = generate_prime_pair(10)
        self.assertEqual(is_prime(pair[0]), True)
        self.assertEqual(is_prime(pair[1]), True)
        self.assertNotEqual(pair[0], pair[1])

    def test_generate_key_pair(self):
        key = generate_key_pair(10)
        self.assertEqual(key[0] != None, True)
        self.assertEqual(key[1] != None, True)
