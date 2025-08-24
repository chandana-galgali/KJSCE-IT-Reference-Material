def shift_cipher_encrypt(message, key):
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

def shift_cipher_decrypt(message, key):
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

stored_users = {}

def register_user():
    username = input("Enter a username: ")
    if username in stored_users:
        print("Username already exists!")
        return
    password = input("Enter a password: ")
    key = int(input("Enter the shift key for encryption: "))
    encrypted_password = shift_cipher_encrypt(password, key)
    stored_users[username] = (encrypted_password, key)
    print("User registered successfully!")

def login_user():
    username = input("Enter your username: ")
    if username not in stored_users:
        print("User does not exist!")
        return
    password = input("Enter your password: ")
    encrypted_password, key = stored_users[username]
    if encrypted_password == shift_cipher_encrypt(password, key):
        print("Login successful!")
    else:
        print("Incorrect password!")

def main():
    while True:
        print("\nMenu:")
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            register_user()
        elif choice == 2:
            login_user()
        elif choice == 3:
            print("Exiting!")
            break
        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()