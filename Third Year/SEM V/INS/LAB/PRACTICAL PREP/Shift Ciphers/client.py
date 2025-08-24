import socket

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

def client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(("localhost", 9999))

    message = input("Enter the message to be sent to the server: ")
    key = int(input("Enter key (integer) to encrypt the message: "))
    encrypted_message = additive_cipher_encrypt(message, key)

    data = f"{encrypted_message}|{key}"

    client_socket.send(data.encode('utf-8'))

    result = client_socket.recv(1024).decode('utf-8')
    print("Decrypted message received from the server: ", result)
    
    client_socket.close()

if __name__ == "__main__":
    client()