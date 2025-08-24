from math import gcd
import random
def is_prime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True
def mod_inverse(a, m):
    m0, x0, x1 = m, 0, 1
    if m == 1:
        return 0
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    if x1 < 0:
        x1 += m0
    return x1
def generate_keys(p, q):
    n = p * q
    phi = (p - 1) * (q - 1)
    e = random.randrange(2, phi)
    while gcd(e, phi) != 1:
        e = random.randrange(2, phi)
    d = mod_inverse(e, phi)
    public_key = (e, n)
    private_key = (d, n)
    return public_key, private_key
def string_to_int_list(text):
    return [ord(char) for char in text]
def int_list_to_string(int_list):
    return ''.join(chr(num) for num in int_list)
def encrypt(int_list, public_key):
    e, n = public_key
    encrypted_message = [pow(char, e, n) for char in int_list]
    return encrypted_message
def decrypt(encrypted_message, private_key):
    d, n = private_key
    decrypted_message = [pow(char, d, n) for char in encrypted_message]
    return decrypted_message
def print_menu():
    print("\nMenu:")
    print("1. Encrypt a message")
    print("2. Decrypt a message")
    print("3. Exit")
def main():
    public_key = None
    private_key = None
    while True:
        print_menu()
        choice = input("Enter your choice (1/2/3): ")
        if choice == '3':
            print("Exiting.")
            break
        if choice in ['1', '2']:
            if public_key is None or private_key is None:
                p = int(input("Enter prime number p: "))
                q = int(input("Enter prime number q: "))
                if not (is_prime(p) and is_prime(q)):
                    print("Both p and q must be prime numbers.")
                    continue
                public_key, private_key = generate_keys(p, q)
                print("Public Key:", public_key)
                print("Private Key:", private_key)
            if choice == '1':
                plaintext = input("Enter the plaintext to encrypt: ")
                int_list = string_to_int_list(plaintext)
                print("Integer Representation of Plaintext:", int_list)
                encrypted_message = encrypt(int_list, public_key)
                print("Encrypted Message:", encrypted_message)
            elif choice == '2':
                encrypted_message = list(map(int, input("Enter the encrypted message as space-separated integers: ").split()))
                decrypted_int_list = decrypt(encrypted_message, private_key)
                decrypted_text = int_list_to_string(decrypted_int_list)
                print("Decrypted Text:", decrypted_text)
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")
if __name__ == "__main__":
    main()