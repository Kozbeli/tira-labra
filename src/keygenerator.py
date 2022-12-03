import random
from primegenerator import generate_prime_pair
from utils import random_between, greatest_common_divisor, modular_inverse


def generate_key_pair(key_size):
    """Luo julkisen ja yksityisen avainparin.

    Args:
        key_size (int): avaimen koko

    Returns:
        tuple: julkisen ja yksityisen avaimen parin
    """

    print(f"\nGenerating key pair with {key_size} bits\n")
    (p, q) = generate_prime_pair(key_size)
    print(f"\nGenerated prime pair: {p}, {q}\n")
    modulus = p * q

    while True:
        public_exponent = random_between(
            pow(2, key_size - 1), pow(2, key_size))
        print(f"\nGenerated random number: {public_exponent}\n")
        if greatest_common_divisor(public_exponent, (p - 1) * (q - 1)) == 1:
            break

    private_exponent = modular_inverse(public_exponent, (p - 1) * (q - 1))
    public_key = (modulus, public_exponent)
    private_key = (modulus, private_exponent)
    return (public_key, private_key)
