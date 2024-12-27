def caesar_cipher(text, shift, mode='encrypt'):
    result = ""
    alphabet = "abcdefghijklmnopqrstuvwxyz"

    for char in text:
        if char.isalpha():
            char = char.lower()
            index = alphabet.find(char)
            if mode == 'encrypt':
                new_index = (index + shift) % 26
            else:
                new_index = (index - shift) % 26
            result += alphabet[new_index]
        else:
            result += char

    return result

def main():
    while True:
        print("\n*** Caesar Cipher Program ***")
        print("1. Encrypt a message")
        print("2. Decrypt a message")
        print("3. Exit")
        choice = input("Enter your choice (1-3): ")

        if choice == '1':
            text = input("Enter the text to encrypt: ")
            shift = int(input("Enter the shift value: "))
            ciphertext = caesar_cipher(text, shift)
            print(f"Ciphertext: {ciphertext}")

        elif choice == '2':
            text = input("Enter the ciphertext to decrypt: ")
            shift = int(input("Enter the shift value: "))
            plaintext = caesar_cipher(text, shift, mode='decrypt')
            print(f"Plaintext: {plaintext}")

        elif choice == '3':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
