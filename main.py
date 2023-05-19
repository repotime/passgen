import random
import string

def generate_password(length, complexity):
    characters = ""

    if complexity == "1":
        characters = string.ascii_letters
    elif complexity == "2":
        characters = string.ascii_letters + string.digits
    elif complexity == "3":
        characters = string.ascii_letters + string.digits + string.punctuation
    else:
        print("Invalid complexity level. Please choose from 1, 2, or 3.")
        return None

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    length = int(input("Enter the length of the password: "))
    complexity = input("Enter the complexity level (1 for letters, 2 for letters and numbers, 3 for letters, numbers, and special characters): ")

    password = generate_password(length, complexity)
    if password:
        print("Generated password:", password)

if __name__ == "__main__":
    main()