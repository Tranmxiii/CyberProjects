import re
import string

def check_password_strength(password):
    strength = 0
    feedback = []

    # Check length
    if len(password) >= 12:
        strength += 2
    elif len(password) >= 8:
        strength += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    # Check for uppercase letters
    if re.search(r'[A-Z]', password):
        strength += 1
    else:
        feedback.append("Add at least one uppercase letter.")

    # Check for lowercase letters
    if re.search(r'[a-z]', password):
        strength += 1
    else:
        feedback.append("Add at least one lowercase letter.")

    # Check for digits
    if re.search(r'\d', password):
        strength += 1
    else:
        feedback.append("Add at least one number.")

    # Check for special characters
    if re.search(r'[!@#$%^&*(),.?\":{}|<>]', password):
        strength += 1
    else:
        feedback.append("Add at least one special character (e.g., !, @, #, $).")

    # Check for common patterns
    common_patterns = ['1234', 'password', 'qwerty', 'abcd', '1111']
    if any(pattern in password.lower() for pattern in common_patterns):
        feedback.append("Avoid common patterns like '1234', 'password', etc.")

    # Evaluate strength
    if strength >= 6:
        return "Strong Password", []
    elif strength >= 4:
        return "Moderate Password", feedback
    else:
        return "Weak Password", feedback

if __name__ == "__main__":
    print("Password Strength Checker")
    print("A password strength checker by Michael Tran")
    print("==========================")

    while True:
        password = input("Enter your password to check: ")
        strength, suggestions = check_password_strength(password)

        print(f"\nPassword Strength: {strength}")
        if suggestions:
            print("\nSuggestions to Improve:")
            for suggestion in suggestions:
                print(f"- {suggestion}")

        # Ask if the user wants to check a new password or exit
        retry = input("\nWould you like to check a new password? (yes/no, default no): ").strip().lower()
        if retry not in ['yes', 'y']:
            break

    # Wait for the user to press Enter twice before closing
    input("\nPress Enter to continue...")
    input("Press Enter again to exit...")
