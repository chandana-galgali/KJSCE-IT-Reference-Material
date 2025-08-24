import socket

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

def handle_client(client_socket):
    try:
        data = client_socket.recv(1024).decode('utf-8')
        encrypted_message, key = data.split('|')

        key = int(key)

        decrypted_message = additive_cipher_decrypt(encrypted_message, key)
        
        print("Decrypted message received from client: ", decrypted_message)

        client_socket.send(decrypted_message.encode('utf-8'))
    
    finally:
        client_socket.close()

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("localhost", 9999))
    server_socket.listen(5)
    print("Server is listening on port 9999.")
    
    while True:
        client_socket, address = server_socket.accept()
        print(f"Connection from {address} has been established.")
        handle_client(client_socket)

if __name__ == "__main__":
    start_server()