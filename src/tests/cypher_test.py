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

    def test_message_can_be_converted_to_bytes(self):
        message_as_bytes = self.cypher.message_to_bytes(self.message)
        self.assertEqual(type(message_as_bytes), bytes)

    def test_bytes_can_be_converted_to_message(self):
        message_as_bytes = self.cypher.message_to_bytes(self.message)
        message_as_string = self.cypher.bytes_to_message(message_as_bytes)
        self.assertEqual(type(message_as_string), str)

    def test_message_can_be_converted_to_int(self):
        message_as_bytes = self.cypher.message_to_bytes(self.message)
        message_as_int = self.cypher.bytes_to_ints(message_as_bytes)
        self.assertEqual(type(message_as_int), int)

    def test_int_can_be_converted_to_bytes(self):
        message_as_bytes = self.cypher.message_to_bytes(self.message)
        message_as_int = self.cypher.bytes_to_ints(message_as_bytes)
        int_as_bytes = self.cypher.int_to_bytes(message_as_int, len(message_as_bytes))
        self.assertEqual(type(int_as_bytes), bytes)
