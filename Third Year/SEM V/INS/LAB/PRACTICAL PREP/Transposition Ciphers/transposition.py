import math

def encrypt_row_transposition(pt, key):
    rows = int(math.ceil(len(pt)/len(key)))
    cols = len(key)
    matrix = [['' for _ in range(cols)] for _ in range(rows)]
    index = 0
    for r in range(rows):
        for c in range(cols):
            if index < len(pt):
                matrix[r][c] = pt[index]
                index += 1
            else:
                matrix[r][c] = 'X'
    key_order = sorted(range(len(key)), key=lambda k: key[k])
    ct = ""
    for col in key_order:
        for row in range(rows):
            ct += matrix[row][col]
    return ct

def decrypt_row_transposition(ct, key):
    rows = int(math.ceil(len(ct)/len(key)))
    cols = len(key)
    matrix = [['' for _ in range(cols)] for _ in range(rows)]
    index = 0
    key_order = sorted(range(len(key)), key=lambda k: key[k])
    for col in key_order:
        for row in range(rows):
            if index < len(ct):
                matrix[row][col] = ct[index]
                index += 1 
    pt = ""
    for r in range(rows):
        for c in range(cols):
            pt += matrix[r][c]
    return pt.rstrip('X')

def encrypt_col_transposition(pt, key):
    rows = len(key)
    cols = int(math.ceil(len(pt)/len(key)))
    matrix = [['' for _ in range(cols)] for _ in range(rows)]
    index = 0
    for c in range(cols):
        for r in range(rows):
            if index < len(pt):
                matrix[r][c] = pt[index]
                index += 1
            else:
                matrix[r][c] = 'X'
    key_order = sorted(range(len(key)), key=lambda k: key[k])
    ct = ""
    for row in key_order:
        for col in range(cols):
            ct += matrix[row][col]
    return ct

def decrypt_col_transposition(ct, key):
    rows = len(key)
    cols = int(math.ceil(len(ct)/len(key)))
    matrix = [['' for _ in range(cols)] for _ in range(rows)]
    index = 0
    key_order = sorted(range(len(key)), key=lambda k: key[k])
    for row in key_order:
        for col in range(cols):
             if index < len(ct):
                matrix[row][col] = ct[index]
                index += 1
    pt = ""
    for c in range(cols):
        for r in range(rows):
            pt += matrix[r][c]
    return pt.rstrip('X')

def encrypt_double_transposition(pt, row_key, col_key):
    first_stage = encrypt_row_transposition(pt, row_key)
    return encrypt_col_transposition(first_stage, col_key)

def decrypt_double_transposition(ct, row_key, col_key):
    first_stage = decrypt_col_transposition(ct, col_key)
    return decrypt_row_transposition(first_stage, row_key)

def main():
    while True:
        print("Menu:")
        print("1. Encrypt Row Transposition Cipher")
        print("2. Decrypt Row Transposition Cipher")
        print("3. Encrypt Column Transposition Cipher")
        print("4. Decrypt Column Transposition Cipher")
        print("5. Encrypt Double Transposition Cipher (Row + Column)")
        print("6. Decrypt Double Transposition Cipher (Column + Row)")
        print("7. Exit")
        choice = int(input("Enter your choice: "))

        if choice in [1, 3, 5]:
            pt = input("Enter the plaintext: ").replace(" ", "")

        if choice in [2, 4, 6]:
            ct = input("Enter the ciphertext: ")

        if choice == 1:
            key = input("Enter the key: ")
            print("Cipher Text: ", encrypt_row_transposition(pt, key))

        elif choice == 2:
            key = input("Enter the key: ")
            print("Plain Text: ", decrypt_row_transposition(ct, key))

        elif choice == 3:
            key = input("Enter the key: ")
            print("Cipher Text: ", encrypt_col_transposition(pt, key))

        elif choice == 4:
            key = input("Enter the key: ")
            print("Plain Text: ", decrypt_col_transposition(ct, key))

        elif choice == 5:
            row_key = input("Enter the row key: ")
            col_key = input("Enter the column key: ")
            print("Cipher Text: ", encrypt_double_transposition(pt, row_key, col_key))

        elif choice == 6:
            row_key = input("Enter the row key: ")
            col_key = input("Enter the column key: ")
            print("Plain Text: ", decrypt_double_transposition(ct, row_key, col_key))
        
        elif choice == 7:
            print("Exiting the program!")
            break

        else:
            print("Invalid Choice!")

if __name__ == "__main__":
    main()