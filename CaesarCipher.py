def caesar_cipher(text, shift, mode):
    result = ""

    for char in text:
        if char.isalpha():
            # Determine whether to encrypt or decrypt based on the mode
            if mode == 'encrypt':
                shift_amount = shift
            elif mode == 'decrypt':
                shift_amount = -shift

            # Apply the shift to the character
            shifted = ord(char) + shift_amount

            # Handle wrap-around for uppercase letters
            if char.isupper():
                if shifted > ord('Z'):
                    shifted -= 26
                elif shifted < ord('A'):
                    shifted += 26
            # Handle wrap-around for lowercase letters
            elif char.islower():
                if shifted > ord('z'):
                    shifted -= 26
                elif shifted < ord('a'):
                    shifted += 26

            # Append the shifted character to the result
            result += chr(shifted)
        else:
            # If the character is not a letter, append it unchanged
            result += char

    return result

def main():
    while True:
        choice = input("Do you want to encrypt or decrypt? (encrypt/decrypt): ").lower()
        if choice not in ['encrypt', 'decrypt']:
            print("Please enter 'encrypt' or 'decrypt'.")
            continue

        message = input("Enter your message: ")
        shift = int(input("Enter the shift value (an integer): "))

        if choice == 'encrypt':
            encrypted_message = caesar_cipher(message, shift, 'encrypt')
            print("Encrypted message:", encrypted_message)
        elif choice == 'decrypt':
            decrypted_message = caesar_cipher(message, shift, 'decrypt')
            print("Decrypted message:", decrypted_message)

        another = input("Do you want to perform another operation? (yes/no): ").lower()
        if another != 'yes':
            break

if __name__ == "__main__":
    main()
