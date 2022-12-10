import random
from primegenerator import generate_prime_pair
from utils import random_between, greatest_common_factor, modular_inverse


class NewKeyGenerator:
    def __init__(self):
        self.public_exponent = 0
        self.private_exponent = 0
        self.modulus = 0

    def generate_key_pair(self, key_size):
        """ Luo julkisen ja yksityisen avainparin.

        Args:
            key_size (int): avaimen koko

        Returns:
            tuple: julkinen ja yksityinen avainpari
        """

        print(f"\nGenerating key pair with {key_size} bits\n")
        (p, q) = generate_prime_pair(key_size)
        print(f"\nGenerated prime pair: {p}, {q}\n")
        modulus = p * q

        while True:
            public_exponent = random_between(
                pow(2, key_size - 1), pow(2, key_size))
            if greatest_common_factor(public_exponent, (p - 1) * (q - 1)) == 1:
                break

        print(f"\nGenerated random number: {public_exponent}\n")
        private_exponent = modular_inverse(public_exponent, (p - 1) * (q - 1))
        self.public_exponent = public_exponent
        self.private_exponent = private_exponent
        self.modulus = modulus

    def get_public_key(self):
        return (self.modulus, self.public_exponent)

    def get_private_key(self):
        return (self.modulus, self.private_exponent)
