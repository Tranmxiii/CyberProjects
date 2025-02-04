# Function to encrypt a message using Caesar Cipher
def encrypt(plaintext, shift):
    encrypted_message = ''
    for char in plaintext:
        if char.isalpha():  # Check if the character is a letter
            shift_base = 65 if char.isupper() else 97  # ASCII value of 'A' or 'a'
            encrypted_message += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            encrypted_message += char  # Non-alphabet characters are not changed
    return encrypted_message

# Function to decrypt a message using Caesar Cipher
def decrypt(ciphertext, shift):
    decrypted_message = ''
    for char in ciphertext:
        if char.isalpha():  # Check if the character is a letter
            shift_base = 65 if char.isupper() else 97  # ASCII value of 'A' or 'a'
            decrypted_message += chr((ord(char) - shift_base - shift) % 26 + shift_base)
        else:
            decrypted_message += char  # Non-alphabet characters are not changed
    return decrypted_message

# Function to handle user interaction
def main():
    while True:
        # Get the choice from the user
        choice = input("Would you like to Encrypt or Decrypt a message? (Enter 'E' for Encrypt, 'D' for Decrypt, 'X' to Exit): ").strip().upper()

        if choice == 'X':
            print("Exiting the program. Goodbye!")
            break

        if choice not in ['E', 'D']:
            print("Invalid choice! Please enter 'E' for Encrypt, 'D' for Decrypt, or 'X' to Exit.")
            continue

        # Get the shift value from the user
        try:
            shift = int(input("Enter the shift value (an integer): "))
        except ValueError:
            print("Invalid input! Please enter a valid integer for the shift value.")
            continue
        
        # Get the text to be encrypted or decrypted
        text = input("Enter the text: ")

        # Encrypt or Decrypt based on user choice
        if choice == 'E':
            encrypted = encrypt(text, shift)
            print(f"Encrypted message: {encrypted}")
        else:
            decrypted = decrypt(text, shift)
            print(f"Decrypted message: {decrypted}")

# Run the program
if __name__ == "__main__":
    main()
