class Cypher:
    """ Luokka, joka sisältää salaus- ja purkufunktiot.

    Attributes:
        message_size (int): viestin koko tavuina
    """
    
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
        message_as_bytes = message.encode()
        self.message_size = len(message_as_bytes)
        bytes_as_int = int.from_bytes(message_as_bytes, byteorder='big')
        return pow(bytes_as_int, exponent, modulus)

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
        int_as_bytes = decrypted_int.to_bytes(self.message_size, byteorder='big')
        decrypted_message = int_as_bytes.decode()
        return decrypted_message
