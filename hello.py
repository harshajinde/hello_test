def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error: Division by zero is not allowed."

def main():
    print("Welcome to the simple arithmetic calculator!")
    
    # Get user input for numbers
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
    except ValueError:
        print("Invalid input. Please enter numeric values.")
        return
    
    # Perform calculations
    print(f"Addition: {num1} + {num2} = {add(num1, num2)}")
    print(f"Subtraction: {num1} - {num2} = {subtract(num1, num2)}")
    print(f"Multiplication: {num1} * {num2} = {multiply(num1, num2)}")
    print(f"Division: {num1} / {num2} = {divide(num1, num2)}")

if __name__ == "__main__":
    main()

