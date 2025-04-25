import random
import string

def generate_password(length, use_letters=True, use_numbers=True, use_symbols=True):
    characters = ''
    
    if use_letters:
        characters += string.ascii_letters
    if use_numbers:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    if not characters:
        return "⚠️ Error: No character types selected."

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def get_boolean_input(prompt):
    while True:
        choice = input(prompt + " (y/n): ").lower()
        if choice in ['y', 'n']:
            return choice == 'y'
        print("❌ Please enter 'y' or 'n'.")

def main():
    print("🔐 Password Generator")

    try:
        length = int(input("🔢 Enter desired password length: "))
        if length <= 0:
            print("⚠️ Password length must be greater than 0.")
            return
    except ValueError:
        print("❌ Please enter a valid number.")
        return

    use_letters = get_boolean_input("Include letters?")
    use_numbers = get_boolean_input("Include numbers?")
    use_symbols = get_boolean_input("Include symbols?")

    password = generate_password(length, use_letters, use_numbers, use_symbols)
    print(f"\n🧪 Your generated password:\n{password}")

if __name__ == "__main__":
    main()
