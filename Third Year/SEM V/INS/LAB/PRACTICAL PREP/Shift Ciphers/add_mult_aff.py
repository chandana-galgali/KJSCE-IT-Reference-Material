def additive_cipher_encrypt(message, key):
    encrypted_message = ""
    for c in message:
        if c.isalpha():
            if c.isupper():
                base = 'A'
            else:
                base = 'a'
            shifted_c = chr((ord(c) - ord(base) + key) % 26 + ord(base))
            encrypted_message += shifted_c
        else:
            encrypted_message += c
    return encrypted_message

def additive_cipher_decrypt(message, key):
    decrypted_message = ""
    for c in message:
        if c.isalpha():
            if c.isupper():
                base = 'A'
            else:
                base = 'a'
            shifted_c = chr((ord(c) - ord(base) - key) % 26 + ord(base))
            decrypted_message += shifted_c
        else:
            decrypted_message += c
    return decrypted_message

def multiplicative_cipher_encrypt(message, key):
    encrypted_message = ""
    for c in message:
        if c.isalpha():
            if c.isupper():
                base = 'A'
            else:
                base = 'a'
            shifted_c = chr((ord(c) - ord(base)) * key % 26 + ord(base))
            encrypted_message += shifted_c
        else:
            encrypted_message += c
    return encrypted_message

def multiplicative_cipher_decrypt(message, key):
    try:
        inverse = pow(key, -1, 26)
    except ValueError:
        return print("Key is not invertible!") 
    decrypted_message = ""
    for c in message:
        if c.isalpha():
            if c.isupper():
                base = 'A'
            else:
                base = 'a'
            shifted_c = chr((ord(c) - ord(base)) * inverse % 26 + ord(base))
            decrypted_message += shifted_c
        else:
            decrypted_message += c
    return decrypted_message

def affine_cipher_encrypt(message, a, b):
    encrypted_message = ""
    for c in message:
        if c.isalpha():
            if c.isupper():
                base = 'A'
            else:
                base = 'a'
            shifted_c = chr(((ord(c) - ord(base)) * a + b) % 26 + ord(base))
            encrypted_message += shifted_c
        else:
            encrypted_message += c
    return encrypted_message

def affine_cipher_decrypt(message, a, b):
    try:
        inverse_a = pow(a, -1, 26)
    except ValueError:
        return print("Key is not invertible!") 
    decrypted_message = ""
    for c in message:
        if c.isalpha():
            if c.isupper():
                base = 'A'
            else:
                base = 'a'
            shifted_c = chr(((ord(c) - ord(base) - b) * inverse_a) % 26 + ord(base))
            decrypted_message += shifted_c
        else:
            decrypted_message += c
    return decrypted_message

def main():
    while True:
        print("Menu:")
        print("1. Additive Cipher Encryption")
        print("2. Additive Cipher Decryption")
        print("3. Multiplicative Cipher Encryption")
        print("4. Multiplicative Cipher Decryption")
        print("5. Affine Cipher Encryption")
        print("6. Affine Cipher Decryption")
        print("7. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            message = input("Enter the message to encrypt: ")
            key = int(input("Enter the key: "))
            print("Encrypted message: ", additive_cipher_encrypt(message, key))

        elif choice == 2:
            message = input("Enter the message to encrypt: ")
            key = int(input("Enter the key: "))
            print("Decrypted message: ", additive_cipher_decrypt(message, key))
            
        elif choice == 3:
            message = input("Enter the message to encrypt: ")
            key = int(input("Enter the key: "))
            print("Encrypted message: ", multiplicative_cipher_encrypt(message, key))

        elif choice == 4:
            message = input("Enter the message to encrypt: ")
            key = int(input("Enter the key: "))
            print("Decrypted message: ", multiplicative_cipher_decrypt(message, key))

        elif choice == 5:
            message = input("Enter the message to encrypt: ")
            a = int(input("Enter the multiplier: "))
            b = int(input("Enter the additive: "))
            print("Encrypted message: ", affine_cipher_encrypt(message, a, b))

        elif choice == 6:
            message = input("Enter the message to encrypt: ")
            a = int(input("Enter the multiplier: "))
            b = int(input("Enter the additive: "))
            print("Decrypted message: ", affine_cipher_decrypt(message, a, b))

        elif choice == 7:
            print("Exiting the program!")
            break

        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()