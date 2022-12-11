import unittest
from cypher import Cypher
from keygenerator import generate_key_pair


class TestCypher(unittest.TestCase):
    def setUp(self):
        self.cypher = Cypher()
        self.message = "Hello Bob!"
        (self.public_key, self.private_key) = generate_key_pair(512)

    def test_message_can_be_encrypted(self):
        encrypted_message = self.cypher.encrypt(self.message, self.public_key)
        self.assertEqual(encrypted_message != self.message, True)
        self.assertEqual(type(encrypted_message), int)

    def test_message_can_be_decrypted(self):
        encrypted_message = self.cypher.encrypt(self.message, self.public_key)
        decrypted_message = self.cypher.decrypt(encrypted_message, self.private_key)
        self.assertEqual(decrypted_message, self.message)
        