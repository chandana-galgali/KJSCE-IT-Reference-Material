import socket
import random

def generate_prime_nos(num):
    while True:
        num = random.randint(100, 200)
        if all(num % i != 0 for i in range(2, int(num ** 0.5) + 1)):
            return num
    
def decrypt(encrypted_message, key):
    decrypted_message = ""
    for c in encrypted_message:
        if c.isalpha():
            if c.isupper():
                base = 'A'
            else:
                base = 'a'
            decrypted_message += chr((ord(c) - ord(base) - key) % 26 + ord(base))
        else:
            decrypted_message += c
    return decrypted_message

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(("localhost", 9999))

num = random.randint(2, 200)
p = generate_prime_nos(num)
g = random.randint(2, p - 1)

print("Chosen prime number is ", p, "and the generator is ", g)

a = random.randint(1, p - 1)
print("Client's secret (a): ", a)

RA = pow(g, a, p)
print("Calculated RA = g^a mod p: ", RA)

data = f'{p}|{g}|{RA}'

client_socket.send(data.encode('utf-8'))

RB = int(client_socket.recv(1024).decode('utf-8'))
print("Received RB from the server: ", RB)

RAB = pow(RB, a, p)
print("Calculated shared key RAB: ", RAB)

encrypted_message = client_socket.recv(1024).decode('utf-8')

decrypted_message = decrypt(encrypted_message, RAB)

print("Message from the server: ", decrypted_message)

client_socket.close()