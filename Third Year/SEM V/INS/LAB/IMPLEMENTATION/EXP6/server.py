from flask import Flask, request, jsonify, send_from_directory
import random
import os

app = Flask(__name__)

# Route to serve the client.html file
@app.route('/')
def serve_client():
    return send_from_directory(os.getcwd(), 'client.html')

# Endpoint for the Diffie-Hellman exchange
@app.route('/exchange', methods=['POST'])
def exchange_keys():
    data = request.json
    if not data:
        print("No data received")
        return jsonify({"error": "No data received"}), 400

    try:
        p = int(data['p'])
        g = int(data['g'])
        RA = int(data['RA'])

        print(f"Received from client - p: {p}, g: {g}, RA: {RA}")

        b = random.randint(1, p-1)
        print(f"Server's secret key (b): {b}")

        RB = pow(g, b, p)
        print(f"Calculated RB (g^b mod p): {RB}")

        KAB = pow(RA, b, p)
        print(f"Calculated shared key KAB: {KAB}")

        return jsonify({"RB": str(RB)})

    except Exception as e:
        print(f"Error: {str(e)}")
        return jsonify({"error": str(e)}), 500

# Endpoint for secure communication
@app.route('/secure_communication', methods=['POST'])
def secure_communication():
    data = request.json
    try:
        shared_key = int(data['shared_key'])
        print(f"Received shared key from client: {shared_key}")

        encrypted_message = additive_cipher_encrypt("Hello from server!", shared_key)
        print(f"Encrypted message to send to client: {encrypted_message}")

        # Decrypting the message back to demonstrate decryption
        decrypted_message = additive_cipher_decrypt(encrypted_message, shared_key)
        print(f"Decrypted message on server-side: {decrypted_message}")

        return jsonify({"encrypted_message": encrypted_message, "decrypted_message": decrypted_message})
    except Exception as e:
        print(f"Error: {str(e)}")
        return jsonify({"error": str(e)}), 500

def additive_cipher_encrypt(message, key):
    return ''.join(chr((ord(char) + key) % 256) for char in message)

def additive_cipher_decrypt(encrypted_message, key):
    return ''.join(chr((ord(char) - key) % 256) for char in encrypted_message)

if __name__ == "__main__":
    print("Server is starting.")
    app.run(debug=True, host='127.0.0.1', port=5500)
    print("Server is running on port 5500.")