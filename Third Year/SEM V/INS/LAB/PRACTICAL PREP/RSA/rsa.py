import random
from math import gcd

def generate_prime_nos(bits):
    while True:
        num = random.getrandbits(bits)
        if (num > 1) and all(num % d != 0 for d in range(2, int(num**0.5) + 1)):
            return num

def generate_key_pair(bits):
    p = generate_prime_nos(bits // 2)
    q = generate_prime_nos(bits // 2)
    n = p * q
    phi = (p - 1) * (q - 1)
    e = random.randrange(2, phi)
    while gcd(e, phi) != 1:
        e = random.randrange(2, phi)
    d = pow(e, -1, phi)
    return ((e, n), (d, n))

def encrypt(alice_public_key, message):
    e, n = alice_public_key
    encrypted_message = [pow(ord(char), e, n) for char in message]
    return encrypted_message

def decrypt(alice_private_key, encrypted_message):
    d, n = alice_private_key
    decrypted_message = ''.join(chr(pow(char, d, n)) for char in encrypted_message)
    return decrypted_message

def main():
    bits = int(input("Enter key size in bits (multiples of 8): "))

    alice_public_key, alice_private_key = generate_key_pair(bits)
    bob_public_key, bob_private_key = generate_key_pair(bits)
    
    print("Alice's Public Key: ", alice_public_key)
    print("Alice's Private Key: ", alice_private_key)
    print("Bob's Public Key: ", bob_public_key)
    print("Bob's Private Key: ", bob_private_key)

    message = input("Enter the message for Bob to encrypt and send to Alice: ")
    
    encrypted_message = encrypt(alice_public_key, message)
    print("Encrypted Message sent from Bob: ", encrypted_message)

    decrypted_message = decrypt(alice_private_key, encrypted_message)
    print("Decrypted Message received by Alice: ", decrypted_message)

if __name__ == "__main__":
    main()