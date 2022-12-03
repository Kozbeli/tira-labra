import unittest
from keygenerator import generate_key_pair

class TestKeyGenerator(unittest.TestCase): 

    def test_generate_key_pair(self):
        key = generate_key_pair(10)
        self.assertEqual(key[0] != None, True)
        self.assertEqual(key[1] != None, True)
