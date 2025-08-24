import hashlib

l = 8
ipad = int('01011100', 2)
opad = int('00110110', 2)
key = int('10000101', 2)
IV = int('11100100', 2)

def xor(a, b, length):
    return format(a ^ b, f'0{length}b')

def hashlib_dummy_hash(binary_string):
    input_bytes = int(binary_string, 2).to_bytes((len(binary_string) + 7) // 8, byteorder='big')
    hash_output = hashlib.sha1(input_bytes).digest()
    truncated_hash = format(hash_output[0], '08b')
    return truncated_hash

def hmac_simple_binary(plaintext, key, IV, ipad, opad, block_size):
    k_xor_ipad = xor(key, ipad, block_size)
    z0 = format(IV, '08b') + k_xor_ipad
    z1 = hashlib_dummy_hash(z0)
    chunks = [plaintext[i:i + block_size] for i in range(0, len(plaintext), block_size)]
    current_hash = z1
    for chunk in chunks:
        z_concat = current_hash + chunk
        current_hash = hashlib_dummy_hash(z_concat)
    k_xor_opad = xor(key, opad, block_size)
    p = format(IV, '08b') + k_xor_opad
    q = hashlib_dummy_hash(p)
    r = q + current_hash
    final_hmac = hashlib_dummy_hash(r)
    return final_hmac

plaintext = '1101100101001100100011011110011101000001010001110001100010111010'
final_hmac_result = hmac_simple_binary(plaintext, key, IV, ipad, opad, l)
print("Final HMAC Output:", final_hmac_result)