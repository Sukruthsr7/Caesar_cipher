def caesar_cipher(text, shift, mode='encrypt'):
    result = ""
    alphabet_lower = "abcdefghijklmnopqrstuvwxyz"
    alphabet_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    digits = "0123456789"
    special_chars = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"

    for char in text:
        if char.islower():
            alphabet = alphabet_lower
        elif char.isupper():
            alphabet = alphabet_upper
        elif char.isdigit():
            alphabet = digits
        elif char in special_chars:
            alphabet = special_chars
        else:
            result += char
            continue

        index = alphabet.find(char)
        if mode == 'encrypt':
            new_index = (index + shift) % len(alphabet)
        else:
            new_index = (index - shift) % len(alphabet)
        
        result += alphabet[new_index]

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
            try:
                shift = int(input("Enter the shift value: "))
                ciphertext = caesar_cipher(text, shift)
                print(f"Ciphertext: {ciphertext}")
            except ValueError:
                print("Invalid shift value. Please enter an integer.")

        elif choice == '2':
            text = input("Enter the ciphertext to decrypt: ")
            try:
                shift = int(input("Enter the shift value: "))
                plaintext = caesar_cipher(text, shift, mode='decrypt')
                print(f"Plaintext: {plaintext}")
            except ValueError:
                print("Invalid shift value. Please enter an integer.")

        elif choice == '3':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
