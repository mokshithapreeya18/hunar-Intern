import os
def caesar_cipher_encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_amount = 65 if char.isupper() else 97
            encrypted_text += chr((ord(char) + shift - shift_amount) % 26 + shift_amount)
        else:
            encrypted_text += char
    return encrypted_text


def caesar_cipher_decrypt_brute_force(text):
    decrypted_texts = []
    for shift in range(1, 26):  # Try all possible shifts
        decrypted_text = ""
        for char in text:
            if char.isalpha():
                shift_amount = 65 if char.isupper() else 97
                decrypted_text += chr((ord(char) - shift - shift_amount) % 26 + shift_amount)
            else:
                decrypted_text += char
        decrypted_texts.append(decrypted_text)
    return decrypted_texts

def encrypt_message():
    message = input("Enter the message to encrypt: ")
    shift = int(input("Enter the shift amount (0-25): "))
    encrypted_message = caesar_cipher_encrypt(message, shift)
    print(f"Encrypted Message: {encrypted_message}")

def decrypt_message():
    message = input("Enter the message to decrypt: ")
    decrypted_texts = caesar_cipher_decrypt_brute_force(message)

    for i, decrypted_text in enumerate(decrypted_texts):
        print(f"Decrypted Message with shift {i + 1}: {decrypted_text}")

def encrypt_file():
    file_path = input("Enter the path of the file to encrypt: ")
    shift = int(input("Enter the shift amount (0-25): "))

    if os.path.isfile(file_path):
        with open(file_path, 'r') as file:
            data = file.read()
        encrypted_data = caesar_cipher_encrypt(data, shift)
        with open(file_path + '.encrypted', 'w') as file:
            file.write(encrypted_data)
        print("File encrypted successfully.")
    else:
        print("File not found.")
def decrypt_file():
    file_path = input("Enter the path of the file to decrypt: ")

    if os.path.isfile(file_path):
        with open(file_path, 'r') as file:
            data = file.read()
        decrypted_texts = caesar_cipher_decrypt_brute_force(data)

        for i, decrypted_text in enumerate(decrypted_texts):
            print(f"Decrypted Message with shift {i + 1}: {decrypted_text}")
    else:
        print("File not found.")

def main():
    print("Welcome to the Simple Encryption and Decryption Tool!")

    while True:
        print("\nMenu:")
        print("1. Encrypt a message")
        print("2. Decrypt a message")
        print("3. Encrypt a file")
        print("4. Decrypt a file")
        print("5. Exit")
        choice = input("Choose an option (1/2/3/4/5): ")

        if choice == '1':
            encrypt_message()
        elif choice == '2':
            decrypt_message()
        elif choice == '3':
            encrypt_file()
        elif choice == '4':
            decrypt_file()
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3, 4, or 5.")


if __name__ == "__main__":
    main()
