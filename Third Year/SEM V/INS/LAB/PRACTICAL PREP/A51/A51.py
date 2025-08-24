class A51:
    def __init__(self, key):
        self.x = [int(b) for b in key[:19]] 
        self.y = [int(b) for b in key[19:41]]
        self.z = [int(b) for b in key[41:]]

    def majority(self, x, y, z):
        return int(x + y + z > 1) 
    
    def step_x(self):
        t = self.x[13] ^ self.x[16] ^ self.x[17] ^ self.x[18]
        self.x = [t] + self.x[:-1]

    def step_y(self):
        t = self.y[20] ^ self.y[21]
        self.y = [t] + self.y[:-1]

    def step_z(self):
        t = self.z[7] ^ self.z[20] ^ self.z[21] ^ self.z[22]
        self.z = [t] + self.z[:-1]
    
    def generate_keystream(self, length):
        keystream = []
        for _ in range(length):
            m = self.majority(self.x[8], self.y[10], self.z[10])
            if self.x[8] == m:
                self.step_x()
            if self.y[10] == m:
                self.step_y()
            if self.z[10] == m:
                self.step_z()
            keystream_bit = self.x[18] ^ self.y[21] ^ self.z[22]
            keystream.append(keystream_bit)
        return keystream

def xor_bitsrings(a, b):
    return [ai ^ bi for ai, bi in zip(a, b)]

def main():

    key = input("Enter 64-bit key as a binary string: ")
    if len(key) != 64 and not all (c in '01' for c in key):
        print("Invalid key!")
        return
    
    plaintext = input("Enter the plaintext as a binary string: ")
    if not all (c in '01' for c in plaintext):
        print("Invalid plaintext!")
        return
    
    cipher = A51(key)
    plaintext_bits = [int (b) for b in plaintext]
    keystream = cipher.generate_keystream(len(plaintext_bits))

    ciphertext_bits = xor_bitsrings(plaintext_bits, keystream)
    ciphertext = ''.join(map(str, ciphertext_bits))
    print("Ciphertext (binary): ", ciphertext)

    cipher = A51(key)
    ciphertext_bits = [int(b) for b in ciphertext]
    decrypted_bits = xor_bitsrings(ciphertext_bits, cipher.generate_keystream(len(ciphertext_bits)))
    decrypted_text = ''.join(map(str, decrypted_bits))
    print("Decrypted text (binary):", decrypted_text)

if __name__ == "__main__":
    main()