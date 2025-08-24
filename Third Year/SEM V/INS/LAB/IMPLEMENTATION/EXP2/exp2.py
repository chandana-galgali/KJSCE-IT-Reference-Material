def pad_text(text, size):
    return text + 'X' * (size - len(text) % size)

def create_matrix(text, rows, cols):
    return [text[i:i + cols] for i in range(0, len(text), cols)]

def permute(matrix, key):
    return [matrix[key.index(i + 1)] for i in range(len(key))]

def inverse_permute(matrix, key):
    inverse_key = sorted(range(len(key)), key=lambda k: key[k])
    return [matrix[inverse_key.index(i)] for i in range(len(key))]

def encrypt_row_transposition(plain_text, rows, cols, row_key):
    plain_text = pad_text(plain_text, rows * cols)
    matrix = create_matrix(plain_text, rows, cols)
    row_key = [int(k) for k in row_key]
    permuted_matrix = permute(matrix, row_key)
    transposed = ''.join([''.join(row) for row in permuted_matrix])
    return transposed

def decrypt_row_transposition(cipher_text, rows, cols, row_key):
    matrix = create_matrix(cipher_text, rows, cols)
    row_key = [int(k) for k in row_key]
    permuted_matrix = inverse_permute(matrix, row_key)
    transposed = ''.join([''.join(row) for row in permuted_matrix])
    return transposed[:rows * cols]

def encrypt_column_transposition(plain_text, rows, cols, col_key):
    if len(col_key) != cols:
        raise ValueError("Key length must match the number of columns.")
    plain_text = pad_text(plain_text, rows * cols)
    matrix = create_matrix(plain_text, rows, cols)
    col_key = [int(k) for k in col_key]
    sorted_col_key = sorted(range(len(col_key)), key=lambda k: col_key[k])
    transposed = ''.join(''.join(row[i] for i in sorted_col_key) for row in matrix)
    return transposed

def decrypt_column_transposition(cipher_text, rows, cols, col_key):
    if len(col_key) != cols:
        raise ValueError("Key length must match the number of columns.")
    num_of_rows = len(cipher_text) // cols
    matrix = create_matrix(cipher_text, num_of_rows, cols)
    col_key = [int(k) for k in col_key]
    sorted_col_key = sorted(range(len(col_key)), key=lambda k: col_key[k])
    transposed = ''.join(''.join(row[sorted_col_key.index(i)] for i in range(len(col_key))) for row in matrix)
    return transposed[:rows * cols]

def double_transposition_encrypt(plain_text, rows, cols, row_key, col_key):
    row_transposed = encrypt_row_transposition(plain_text, rows, cols, row_key)
    double_transposed = encrypt_column_transposition(row_transposed, rows, cols, col_key)
    return double_transposed

def double_transposition_decrypt(cipher_text, rows, cols, row_key, col_key):
    col_transposed = decrypt_column_transposition(cipher_text, rows, cols, col_key)
    double_transposed = decrypt_row_transposition(col_transposed, rows, cols, row_key)
    return double_transposed

def menu():
    while True:
        print("\nMenu:")
        print("1. Encrypt Row Transposition Cipher")
        print("2. Decrypt Row Transposition Cipher")
        print("3. Encrypt Column Transposition Cipher")
        print("4. Decrypt Column Transposition Cipher")
        print("5. Encrypt Double Transposition Cipher")
        print("6. Decrypt Double Transposition Cipher")
        print("7. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 7:
            break

        if choice in [1, 3, 5]:
            plain_text = input("Enter the plaintext: ").replace(" ", "")
            rows = int(input("Enter the number of rows: "))
            cols = int(input("Enter the number of columns: "))
        
        if choice in [2, 4, 6]:
            cipher_text = input("Enter the cipher text: ")
            rows = int(input("Enter the number of rows: "))
            cols = int(input("Enter the number of columns: "))

        if choice == 1:
            row_key = input("Enter the row key: ")
            cipher_text = encrypt_row_transposition(plain_text, rows, cols, row_key)
            print(f"Cipher Text: {cipher_text}")
        elif choice == 2:
            row_key = input("Enter the row key: ")
            decrypted_text = decrypt_row_transposition(cipher_text, rows, cols, row_key)
            print(f"Decrypted Text: {decrypted_text}")
        elif choice == 3:
            col_key = input("Enter the column key: ")
            cipher_text = encrypt_column_transposition(plain_text, rows, cols, col_key)
            print(f"Cipher Text: {cipher_text}")
        elif choice == 4:
            col_key = input("Enter the column key: ")
            decrypted_text = decrypt_column_transposition(cipher_text, rows, cols, col_key)
            print(f"Decrypted Text: {decrypted_text}")
        elif choice == 5:
            row_key = input("Enter the row key: ")
            col_key = input("Enter the column key: ")
            cipher_text = double_transposition_encrypt(plain_text, rows, cols, row_key, col_key)
            print(f"Cipher Text: {cipher_text}")
        elif choice == 6:
            row_key = input("Enter the row key: ")
            col_key = input("Enter the column key: ")
            decrypted_text = double_transposition_decrypt(cipher_text, rows, cols, row_key, col_key)
            print(f"Decrypted Text: {decrypted_text}")
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    menu()