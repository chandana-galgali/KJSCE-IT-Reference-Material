#include <iostream>
#include <string>
using namespace std;

string additiveCipherEncrypt(string message, int key) {
    string encryptedMessage = "";
    for (char& c : message) {
        if (isalpha(c)) {
            char base = isupper(c) ? 'A' : 'a';
            char shifted = (c - base + key) % 26 + base;
            encryptedMessage += shifted;
        } else {
            encryptedMessage += c;
        }
    }
    return encryptedMessage;
}

string additiveCipherDecrypt(string encryptedMessage, int key) {
    string decryptedMessage = "";
    for (char& c : encryptedMessage) {
        if (isalpha(c)) {
            char base = isupper(c) ? 'A' : 'a';
            char shifted = (c - base - key + 26) % 26 + base;
            decryptedMessage += shifted;
        } else {
            decryptedMessage += c;
        }
    }
    return decryptedMessage;
}

string multiplicativeCipherEncrypt(string message, int key) {
    string encryptedMessage = "";
    for (char& c : message) {
        if (isalpha(c)) {
            char base = isupper(c) ? 'A' : 'a';
            char shifted = (c - base) * key % 26 + base;
            encryptedMessage += shifted;
        } else {
            encryptedMessage += c;
        }
    }
    return encryptedMessage;
}

int findMultiplicativeInverse(int key, int mod) {
    for (int i = 1; i < mod; ++i) {
        if ((key * i) % mod == 1) {
            return i;
        }
    }
    return -1; // No inverse exists
}

string multiplicativeCipherDecrypt(string encryptedMessage, int key) {
    int inverse = findMultiplicativeInverse(key, 26);
    if (inverse == -1) {
        return "Error: No multiplicative inverse found.";
    }
    string decryptedMessage = "";
    for (char& c : encryptedMessage) {
        if (isalpha(c)) {
            char base = isupper(c) ? 'A' : 'a';
            char shifted = (c - base) * inverse % 26 + base;
            decryptedMessage += shifted;
        } else {
            decryptedMessage += c;
        }
    }
    return decryptedMessage;
}

string affineCipherEncrypt(string message, int key_m, int key_a) {
    string encryptedMessage = "";
    for (char& c : message) {
        if (isalpha(c)) {
            char base = isupper(c) ? 'A' : 'a';
            char shifted = ((c - base) * key_m + key_a) % 26 + base;
            encryptedMessage += shifted;
        } else {
            encryptedMessage += c;
        }
    }
    return encryptedMessage;
}

string affineCipherDecrypt(string encryptedMessage, int key_m, int key_a) {
    int inverse = findMultiplicativeInverse(key_m, 26);
    if (inverse == -1) {
        return "Error: No multiplicative inverse found.";
    }
    string decryptedMessage = "";
    for (char& c : encryptedMessage) {
        if (isalpha(c)) {
            char base = isupper(c) ? 'A' : 'a';
            char shifted = (inverse * ((c - base) - key_a + 26)) % 26 + base;
            decryptedMessage += shifted;
        } else {
            decryptedMessage += c;
        }
    }
    return decryptedMessage;
}

int main() {
    int choice;
    string message;
    int key, key_m, key_a;

    do {
        cout << "Menu:" << endl;
        cout << "1. Additive Cipher Encryption" << endl;
        cout << "2. Additive Cipher Decryption" << endl;
        cout << "3. Multiplicative Cipher Encryption" << endl;
        cout << "4. Multiplicative Cipher Decryption" << endl;
        cout << "5. Affine Cipher Encryption" << endl;
        cout << "6. Affine Cipher Decryption" << endl;
        cout << "7. Exit" << endl;
        cout << "Enter your choice: ";
        cin >> choice;

        switch (choice) {
            case 1:
                cout << "Enter message to encrypt: ";
                cin.ignore();
                getline(cin, message);
                cout << "Enter key (integer): ";
                cin >> key;
                cout << "Encrypted message: " << additiveCipherEncrypt(message, key) << endl;
                break;
            case 2:
                cout << "Enter message to decrypt: ";
                cin.ignore();
                getline(cin, message);
                cout << "Enter key (integer): ";
                cin >> key;
                cout << "Decrypted message: " << additiveCipherDecrypt(message, key) << endl;
                break;
            case 3:
                cout << "Enter message to encrypt: ";
                cin.ignore();
                getline(cin, message);
                cout << "Enter key (integer): ";
                cin >> key;
                cout << "Encrypted message: " << multiplicativeCipherEncrypt(message, key) << endl;
                break;
            case 4:
                cout << "Enter message to decrypt: ";
                cin.ignore();
                getline(cin, message);
                cout << "Enter key (integer): ";
                cin >> key;
                cout << "Decrypted message: " << multiplicativeCipherDecrypt(message, key) << endl;
                break;
            case 5:
                cout << "Enter message to encrypt: ";
                cin.ignore();
                getline(cin, message);
                cout << "Enter multiplier (integer): ";
                cin >> key_m;
                cout << "Enter additive (integer): ";
                cin >> key_a;
                cout << "Encrypted message: " << affineCipherEncrypt(message, key_m, key_a) << endl;
                break;
            case 6:
                cout << "Enter message to decrypt: ";
                cin.ignore();
                getline(cin, message);
                cout << "Enter multiplier (integer): ";
                cin >> key_m;
                cout << "Enter additive (integer): ";
                cin >> key_a;
                cout << "Decrypted message: " << affineCipherDecrypt(message, key_m, key_a) << endl;
                break;
            case 7:
                cout << "Exiting the program." << endl;
                break;
            default:
                cout << "Invalid choice! Please try again." << endl;
                break;
        }
    } while (choice != 7);

    return 0;
}