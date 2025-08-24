import socket

def mod_exp(number, mod):
    return number % mod

def client():
    R_a = 1567

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(("localhost", 9999))

    R_b = int(client_socket.recv(1024).decode('utf-8'))
    print("Client received R_b = ", R_b, " from server.")

    remainder_from_client = mod_exp(R_a, R_b)
    print("Client computed remainder: ", remainder_from_client)

    client_socket.send(str(remainder_from_client).encode('utf-8'))

    auth_result = client_socket.recv(1024).decode()
    print("Authentication result from server: ", auth_result)

    client_socket.close()

if __name__ == "__main__":
    client()