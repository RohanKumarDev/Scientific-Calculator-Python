import math

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

def power(x, y):
    return x ** y

def square_root(x):
    return math.sqrt(x)

def logarithm(x, base):
    return math.log(x, base)

def sin(x):
    return math.sin(math.radians(x))

def cos(x):
    return math.cos(math.radians(x))

def tan(x):
    return math.tan(math.radians(x))

def calculate():
    print("Scientific Calculator")
    print("Operations:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Power")
    print("6. Square Root")
    print("7. Logarithm")
    print("8. Sine")
    print("9. Cosine")
    print("10. Tangent")

    choice = int(input("Enter operation number (1-10): "))

    if choice in [1, 2, 3, 4, 5]:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

    if choice == 1:
        result = add(num1, num2)
        print("Result:", result)
    elif choice == 2:
        result = subtract(num1, num2)
        print("Result:", result)
    elif choice == 3:
        result = multiply(num1, num2)
        print("Result:", result)
    elif choice == 4:
        result = divide(num1, num2)
        print("Result:", result)
    elif choice == 5:
        result = power(num1, num2)
        print("Result:", result)
    elif choice == 6:
        num = float(input("Enter a number: "))
        result = square_root(num)
        print("Result:", result)
    elif choice == 7:
        num = float(input("Enter a number: "))
        base = float(input("Enter the logarithm base: "))
        result = logarithm(num, base)
        print("Result:", result)
    elif choice == 8:
        angle = float(input("Enter an angle in degrees: "))
        result = sin(angle)
        print("Result:", result)
    elif choice == 9:
        angle = float(input("Enter an angle in degrees: "))
        result = cos(angle)
        print("Result:", result)
    elif choice == 10:
        angle = float(input("Enter an angle in degrees: "))
        result = tan(angle)
        print("Result:", result)
    else:
        print("Invalid choice!")

    # Ask for input again
    again = input("Perform another calculation? (yes/no): ")
    if again.lower() == "yes":
        calculate()

calculate()
