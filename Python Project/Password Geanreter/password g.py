import random
import string

def generate_password(length, include_lowercase=True, include_uppercase=True, include_digits=True, include_special_chars=True):
    characters = ''
    if include_lowercase:
        characters += string.ascii_lowercase
    if include_uppercase:
        characters += string.ascii_uppercase
    if include_digits:
        characters += string.digits
    if include_special_chars:
        characters += string.punctuation

    if not characters:
        return "Error: No characters selected."

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("=== Random Password Generator ===")
    length = int(input("Enter the desired password length: "))
    include_lowercase = input("Include lowercase letters? (y/n): ").lower() == "y"
    include_uppercase = input("Include uppercase letters? (y/n): ").lower() == "y"
    include_digits = input("Include digits? (y/n): ").lower() == "y"
    include_special_chars = input("Include special characters? (y/n): ").lower() == "y"

    password = generate_password(length, include_lowercase, include_uppercase, include_digits, include_special_chars)
    print("Generated Password:", password)

if __name__ == "__main__":
    main()
