class Cypher:
    def __init__(self):
        self.message_size = 0

    def encrypt(self, message, *public_key):
        """ Salaa viestin.

        Args:
            message (str): viesti
            public_key (tuple): julkinen avain

        Returns:
            int: salattu viesti
        """

        exponent = public_key[0][1]
        modulus = public_key[0][0]

        self.message_size = len(message.encode('utf8'))
        bytes = self.message_to_bytes(message)
        int = self.bytes_to_ints(bytes)
        return pow(int, exponent, modulus)

    def decrypt(self, message, *private_key):
        """ Purkaa viestin.

        Args:
            message (int): salattu viesti
            private_key (tuple): yksityinen avain

        Returns:
            str: purettu viesti
        """

        exponent = private_key[0][1]
        modulus = private_key[0][0]
        decrypted_int = pow(message, exponent, modulus)
        bytes = self.int_to_bytes(decrypted_int, self.message_size)
        message = self.bytes_to_message(bytes)
        return message

    def message_to_bytes(self, message):
        """ Muuntaa viestin tavuiksi.

        Args:
            message (str): viesti

        Returns:
            bytes: viesti tavuina
        """

        return message.encode('utf8')

    def bytes_to_message(self, bytes):
        """ Muuntaa tavut viestiksi.

        Args:
            bytes (bytes): viesti tavuina

        Returns:
            str: viesti
        """

        return bytes.decode('utf8')

    def bytes_to_ints(self, bytes):
        """ Muuntaa tavut kokonaisluvuiksi.

        Args:
            bytes (bytes): viesti tavuina

        Returns:
            int: viesti kokonaislukuna
        """

        return int.from_bytes(bytes, byteorder='big')

    def int_to_bytes(self, int, size):
        """ Muuntaa kokonaisluvun tavuiksi.

        Args:
            int (int): viesti kokonaislukuna
            size (int): viestin koko tavuina

        Returns:
            bytes: viesti tavuina
        """

        return int.to_bytes(size, byteorder='big')
