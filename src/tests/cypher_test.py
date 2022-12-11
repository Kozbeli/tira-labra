import unittest
from cypher import Cypher
from keygenerator import KeyGenerator


class TestCypher(unittest.TestCase):
    def setUp(self):
        key_generator = KeyGenerator()
        key_generator.generate_key_pair(512)
        self.public_key = key_generator.get_public_key()
        self.private_key = key_generator.get_private_key()
        self.cypher = Cypher()
        self.message = "Hello Bob!"

    def test_encrypt(self):
        encrypted_message = self.cypher.encrypt(self.message, self.public_key)
        self.assertEqual(encrypted_message != 0, True)

    def test_decrypt(self):
        encrypted_message = self.cypher.encrypt(self.message, self.public_key)
        decrypted_message = self.cypher.decrypt(
            encrypted_message, self.private_key)
        self.assertEqual(decrypted_message, self.message)
