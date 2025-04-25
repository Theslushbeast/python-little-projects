def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "⚠️ Cannot divide by zero!"
    return a / b

def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("❌ Invalid input. Please enter a number.")

def main():
    while True:
        print("\n--- Simple Calculator ---")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
        print("5. Exit")

        choice = input("👉 Choose an operation (1-5): ")

        if choice == "5":
            print("👋 Goodbye!")
            break

        if choice in {"1", "2", "3", "4"}:
            num1 = get_number("🔢 Enter first number: ")
            num2 = get_number("🔢 Enter second number: ")

            if choice == "1":
                result = add(num1, num2)
                symbol = "+"
            elif choice == "2":
                result = subtract(num1, num2)
                symbol = "-"
            elif choice == "3":
                result = multiply(num1, num2)
                symbol = "*"
            elif choice == "4":
                result = divide(num1, num2)
                symbol = "/"

            print(f"🧮 Result: {num1} {symbol} {num2} = {result}")
        else:
            print("❌ Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
