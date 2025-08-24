import socket
import random

def mod_exp(number, mod):
    return number % mod

def server():
    R_a = 1567 

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("localhost", 9999))
    server_socket.listen(5)
    print("Server is listening on port 9999.")

    conn, addr = server_socket.accept()
    print("Connected by client at ", addr)

    R_b = random.randint(100, 999)
    print("Server sends R_b = ", R_b, " to client.")
    conn.send(str(R_b).encode('utf-8'))

    response = conn.recv(1024).decode('utf-8')
    remainder_from_client = int(response)
    print("Received client's remainder: ", remainder_from_client)

    remainder_from_server = mod_exp(R_a, R_b)
    print("Server's computed remainder: ", remainder_from_server)

    if remainder_from_client == remainder_from_server:
        print("Authentication successful!")
        conn.send("Authentication successful!".encode('utf-8'))
    else:
        print("Authentication failed.")
        conn.send("Authentication failed!".encode('utf-8')) 

    conn.close()
    server_socket.close()

if __name__ == "__main__":
    server()