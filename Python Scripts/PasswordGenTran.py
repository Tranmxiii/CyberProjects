import random
import string

def generate_password(length=16, use_uppercase=True, use_numbers=True, use_special_chars=True):
    characters = string.ascii_lowercase

    if use_uppercase:
        characters += string.ascii_uppercase
    if use_numbers:
        characters += string.digits
    if use_special_chars:
        characters += string.punctuation

    if not characters:
        raise ValueError("No character sets selected for password generation.")

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

if __name__ == "__main__":
    while True:
        print("Welcome to Tran Gen, a password generator by Michael Tran")
        print("==========================")

        try:
            length = int(input("Enter password length (default 16): ") or 16)
        except ValueError:
            print("Invalid input. Using default length (16).")
            length = 16

        use_uppercase = input("Include uppercase letters? (yes/no, default yes): ").strip().lower() in ['yes', 'y', '']
        use_numbers = input("Include numbers? (yes/no, default yes): ").strip().lower() in ['yes', 'y', '']
        use_special_chars = input("Include special characters? (yes/no, default yes): ").strip().lower() in ['yes', 'y', '']

        try:
            num_passwords = int(input("How many passwords would you like to generate? (default 1): ") or 1)
        except ValueError:
            print("Invalid input. Generating 1 password.")
            num_passwords = 1

        print("\nGenerated Password(s):")
        print("===================")
        for _ in range(num_passwords):
            password = generate_password(length, use_uppercase, use_numbers, use_special_chars)
            print(password)

        # Ask if the user wants to generate new passwords or exit
        retry = input("\nWould you like to generate new passwords? (yes/no, default no): ").strip().lower()
        if retry not in ['yes', 'y']:
            break

    # Wait for the user to press Enter twice before closing
    input("\nPress Enter to continue...")
    input("Press Enter again to exit...")
