import random

# Optimized function to check if a number is prime
def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    
    # Use 6k +/- 1 optimization for larger primes
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

# Optimized function to generate a large prime number
def generate_large_prime(key_size):
    while True:
        # Generate a random odd number of the specified size
        num = random.getrandbits(key_size) | 1  # Ensures the number is odd
        if is_prime(num):
            return num

# Function to calculate the greatest common divisor (GCD)
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Optimized function to find the modular inverse of e mod phi using the Extended Euclidean Algorithm
def mod_inverse(e, phi):
    def egcd(a, b):
        if a == 0:
            return b, 0, 1
        g, x1, y1 = egcd(b % a, a)
        return g, y1 - (b // a) * x1, x1

    g, x, _ = egcd(e, phi)
    if g != 1:
        raise Exception('Modular inverse does not exist')
    else:
        return x % phi

# Function to generate public and private keys
def generate_keypair(key_size):
    p = generate_large_prime(key_size // 2)  # Typically, use key_size // 2 for p and q
    q = generate_large_prime(key_size // 2)
    n = p * q
    phi = (p - 1) * (q - 1)

    # Choose e such that 1 < e < phi and e is coprime to phi
    e = random.randrange(2, phi)
    while gcd(e, phi) != 1:
        e = random.randrange(2, phi)

    d = mod_inverse(e, phi)

    return ((e, n), (d, n))

# Function to encrypt the message
def encrypt(public_key, plaintext):
    e, n = public_key
    ciphertext = [pow(ord(char), e, n) for char in plaintext]
    return ciphertext

# Function to decrypt the message
def decrypt(private_key, ciphertext):
    d, n = private_key
    plaintext = ''.join([chr(pow(char, d, n)) for char in ciphertext])
    return plaintext

# Function to sign a message (Non-Repudiation)
def sign(private_key, message):
    d, n = private_key
    signature = [pow(ord(char), d, n) for char in message]
    return signature

# Function to verify a signature
def verify(public_key, message, signature):
    e, n = public_key
    decrypted_signature = ''.join([chr(pow(char, e, n)) for char in signature])
    return decrypted_signature == message

def main():
    # Take key size as input from the user
    key_size = int(input("Enter the key size in bits: "))

    # Generate key pairs for Alice (sender) and Bob (receiver)
    print("Generating key pairs.")
    alice_public_key, alice_private_key = generate_keypair(key_size)
    bob_public_key, bob_private_key = generate_keypair(key_size)

    print(f"Alice's Public Key: {alice_public_key}")
    print(f"Alice's Private Key: {alice_private_key}")
    print(f"Bob's Public Key: {bob_public_key}")
    print(f"Bob's Private Key: {bob_private_key}")

    # Input the message
    message = input("Enter the message to send: ")

    # Encrypt the message using Bob's public key
    encrypted_message = encrypt(bob_public_key, message)
    print("Encrypted message:", encrypted_message)

    # Convert the encrypted message integers to strings (to avoid OverflowError)
    encrypted_message_str = ','.join(map(str, encrypted_message))

    # Sign the encrypted message using Alice's private key (non-repudiation)
    signature = sign(alice_private_key, encrypted_message_str)
    print("Encrypted message signed successfully by Alice.")

    # Verify the signature using Alice's public key
    if verify(alice_public_key, encrypted_message_str, signature):
        print("Signature verified successfully. Non-repudiation ensured.")

        # Decrypt the message using Bob's private key
        decrypted_message = decrypt(bob_private_key, encrypted_message)
        print("Decrypted message by Bob:", decrypted_message)
    else:
        print("Signature verification failed. Non-repudiation could not be ensured.")

if __name__ == "__main__":
    main()