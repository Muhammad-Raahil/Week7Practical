import math

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
        return "Error! Division by zero."

def cosine(x):
    return math.cos(math.radians(x))

def sine(x):
    return math.sin(math.radians(x))

def tangent(x):
    return math.tan(math.radians(x))

def main():
    print("Scientific Calculator")
    print("Select operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Cosine")
    print("6. Sine")
    print("7. Tangent")

    while True:
        choice = input("Enter choice (1/2/3/4/5/6/7): ")

        if choice in ['1', '2', '3', '4']:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == '1':
                print(f"{num1} + {num2} = {add(num1, num2)}")
            elif choice == '2':
                print(f"{num1} - {num2} = {subtract(num1, num2)}")
            elif choice == '3':
                print(f"{num1} * {num2} = {multiply(num1, num2)}")
            elif choice == '4':
                print(f"{num1} / {num2} = {divide(num1, num2)}")

        elif choice in ['5', '6', '7']:
            angle = float(input("Enter angle in degrees: "))

            if choice == '5':
                print(f"Cosine of {angle}° = {cosine(angle)}")
            elif choice == '6':
                print(f"Sine of {angle}° = {sine(angle)}")
            elif choice == '7':
                print(f"Tangent of {angle}° = {tangent(angle)}")

        else:
            print("Invalid input. Please try again.")

        next_calculation = input("Do you want to perform another calculation? (yes/no): ")
        if next_calculation.lower() != 'yes':
            break

if __name__ == "__main__":
    main()
