class Cypher:
    def __init__(self):
        self.message_size = 0

    def encrypt(self, message, *public_key):
        exponent = public_key[0][1]
        modulus = public_key[0][0]
        

        # message_as_bytes = self.message_to_bytes(message)
        # bytes_as_int = self.bytes_to_ints(message_as_bytes)
        message_as_bytes = message.encode('utf8')
        self.message_size = len(message_as_bytes)
        bytes_as_int = int.from_bytes(message_as_bytes, byteorder='big')
        return pow(bytes_as_int, exponent, modulus)

    def decrypt(self, message, *private_key):
        exponent = private_key[0][1]
        modulus = private_key[0][0]
        decrypted_int = pow(message, exponent, modulus)
        # bytes = self.int_to_bytes(decrypted_int, self.message_size)
        # message = self.bytes_to_message(bytes)
        int_as_bytes = decrypted_int.to_bytes(self.message_size, byteorder='big')
        decrypted_message = int_as_bytes.decode('utf8')
        return decrypted_message

    def message_to_bytes(self, message):
        return message.encode('utf8')

    def bytes_to_message(self, bytes):
        # return bytes.decode('utf8')
        return int_as_bytes.decode('utf8')

    def bytes_to_ints(self, bytes):
        # return int.from_bytes(bytes, byteorder='big')
        return int.from_bytes(message_as_bytes, byteorder='big')

    def int_to_bytes(self, int, size):
        # return int.to_bytes(size, byteorder='big')
        return decrypted_int.to_bytes(self.message_size, byteorder='big')
