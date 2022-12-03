class Cypher:
    def __init__(self):
        self.message_size = 0

    def encrypt(self, message, *public_key):
        exponent = public_key[0][1]
        modulus = public_key[0][0]

        self.message_size = len(message.encode('utf8'))
        bytes = self.message_to_bytes(message)
        int = self.bytes_to_ints(bytes)
        return pow(int, exponent, modulus)

    def decrypt(self, message, *private_key):
        exponent = private_key[0][1]
        modulus = private_key[0][0]
        decrypted_int = pow(message, exponent, modulus)
        bytes = self.int_to_bytes(decrypted_int, self.message_size)
        message = self.bytes_to_message(bytes)
        return message

    def message_to_bytes(self, message):
        return message.encode('utf8')

    def bytes_to_message(self, bytes):
        return bytes.decode('utf8')

    def bytes_to_ints(self, bytes):
        return int.from_bytes(bytes, byteorder='big')

    def int_to_bytes(self, int, size):
        return int.to_bytes(size, byteorder='big')
