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

def sign(alice_private_key, message):
    d, n = alice_private_key
    signed_message = [pow(ord(char), d, n) for char in message]
    return signed_message

def verify(alice_public_key, signed_message):
    e, n = alice_public_key
    verified_message = ''.join(chr(pow(char, e, n)) for char in signed_message)
    return verified_message

def main():
    bits = int(input("Enter key size in bits (multiples of 8): "))

    alice_public_key, alice_private_key = generate_key_pair(bits)
    bob_public_key, bob_private_key = generate_key_pair(bits)
    
    print("Alice's Public Key: ", alice_public_key)
    print("Alice's Private Key: ", alice_private_key)
    print("Bob's Public Key: ", bob_public_key)
    print("Bob's Private Key: ", bob_private_key)

    message = input("Enter the message for Alice to sign and send to Bob: ")
    
    signature = sign(alice_private_key, message)
    print("Message after being signed by Alice: ", signature)

    verified_message = verify(alice_public_key, signature)

    if verified_message == message:
         print("Signature verified. The following message is sent by Alice:\n", verified_message)
    else:
         print("Signature verification failed. Message is not sent by Alice.")

if __name__ == "__main__":
    main()