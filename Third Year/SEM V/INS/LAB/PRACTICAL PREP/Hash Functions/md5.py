import hashlib

def md5_binary(binary_input):
    input_bytes = int(binary_input, 2).to_bytes((len(binary_input) + 7) // 8, byteorder='big')
    md5_hash = hashlib.md5(input_bytes).digest()
    md5_binary = ''.join(format(byte, '08b') for byte in md5_hash)
    return md5_binary

binary_input = '1101100101001100100011011110011101000001010001110001100010111010' 
md5_result = md5_binary(binary_input)
print("MD5 hash in binary:", md5_result)