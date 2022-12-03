from cypher import Cypher
from keygenerator import generate_key_pair
import rsa


def main():
    cypher = Cypher()
    (public_key, private_key) = generate_key_pair(2048)
    print(f"\nAlice's public key: {public_key}\n")
    print(f"\nAlice's private key: {private_key}\n")

    alice_message = "Hello Bob!"
    print(f"\nAlice's message: {alice_message}\n")

    alice_encrypted = cypher.encrypt(alice_message, public_key)
    print(f"\nAlice's encrypted message: {alice_encrypted}\n")

    alice_decrypted = cypher.decrypt(alice_encrypted, private_key)
    print(f"\nAlice's decrypted message: {alice_decrypted}\n")


if __name__ == "__main__":
    main()
