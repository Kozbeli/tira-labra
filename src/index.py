from primes import generate_primes, sieve_of_eratosthenes
from keygenerator import generate_key_pair
import rsa


def main():
  (alice_public, alice_private) = generate_key_pair(1024)
  print(f"\nAlice's public key: {alice_public}\n")
  print(f"\nAlice's private key: {alice_private}\n")

  (bob_public, bob_private) = rsa.newkeys(512)
  print(f"\nBob's public key: {bob_public}\n")
  print(f"\nBob's private key: {bob_private}\n")

  message = "hello Bob!".encode('utf8')
  print(f"\nmessage: {message}\n")

  encrypted_message = rsa.encrypt(message, alice_public)
  print(f"encrypted message: {encrypted_message}\n")

  decrypted_message = rsa.decrypt(encrypted_message, bob_private)
  print(f"decrypted message: {decrypted_message.decode('utf8')}\n")


if __name__ == "__main__":
  main()