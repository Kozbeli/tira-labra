import unittest
from newkeygenerator import NewKeyGenerator

class TestNewKeyGenerator(unittest.TestCase):
    def setUp(self):
        self.key_generator = NewKeyGenerator()

    def test_key_generator_is_initialized(self):
        self.assertEqual(self.key_generator.modulus, 0)
        self.assertEqual(self.key_generator.public_exponent, 0)
        self.assertEqual(self.key_generator.private_exponent, 0)

    def test_key_pair_can_be_generated(self):
        self.key_generator.generate_key_pair(10)
        self.assertEqual(self.key_generator.modulus != 0, True)
        self.assertEqual(self.key_generator.public_exponent != 0, True)
        self.assertEqual(self.key_generator.private_exponent != 0, True)

    def test_get_public_key(self):
        public_key = self.key_generator.get_public_key()
        self.assertEqual(public_key[0], 0)
        self.assertEqual(public_key[1], 0)

    def test_get_private_key(self):
        private_key = self.key_generator.get_private_key()
        self.assertEqual(private_key[0], 0)
        self.assertEqual(private_key[1], 0)