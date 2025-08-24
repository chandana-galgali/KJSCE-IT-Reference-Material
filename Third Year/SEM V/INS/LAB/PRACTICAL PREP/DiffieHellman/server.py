import socket
import random
    
def encrypt(message, key):
    encrypted_message = ""
    for c in message:
        if c.isalpha():
            if c.isupper():
                base = 'A'
            else:
                base = 'a'
            encrypted_message += chr((ord(c) - ord(base) + key) % 26 + ord(base))
        else:
            encrypted_message += c
    return encrypted_message

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("localhost", 9999))
server_socket.listen(5)
print("Server is listening on port 9999.")

conn, addr = server_socket.accept()
print("Connected to client at ", addr)

data = conn.recv(1024).decode('utf-8')
p, g, RA = data.split('|')

p = int(p)
g = int(g)
RA = int(RA)

print("Received from client:\np = ", p, "\ng = ", g, "\nRA = ", RA)

b = random.randint(1, p - 1)
print("Server's secret (b): ", b)

RB = pow(g, b, p)
print("Calculated RB = g^b mod p: ", RB)

conn.send(str(RB).encode('utf-8'))

RAB = pow(RA, b, p)
print("Calculated shared key RAB: ", RAB)

message = "Hello from Server!"

encrypted_message = encrypt(message, RAB)

conn.send(encrypted_message.encode('utf-8'))

server_socket.close()
conn.close()