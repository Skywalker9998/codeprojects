import math

class CalculatorError(Exception):
    """Custom exception for calculator errors."""
    pass

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise CalculatorError("Division by zero is not allowed.")
    return a / b

def exponentiate(a, b):
    return a ** b

def square_root(a):
    if a < 0:
        raise CalculatorError("Square root of a negative number is not allowed.")
    return math.sqrt(a)

def sine(a):
    return math.sin(math.radians(a))

def cosine(a):
    return math.cos(math.radians(a))

def tangent(a):
    return math.tan(math.radians(a))

def calculator():
    print("=== Python Calculator ===")
    print("""
Available Operations:
1. Addition (+)
2. Subtraction (-)
3. Multiplication (*)
4. Division (/)
5. Exponentiation (^)
6. Square Root (√)
7. Sine (sin)
8. Cosine (cos)
9. Tangent (tan)
10. Exit
""")

    while True:
        try:
            choice = int(input("Enter the number corresponding to the operation: "))
            
            if choice == 10:
                print("Goodbye!")
                break
            
            if choice in [1, 2, 3, 4, 5]:  # Binary operations
                num1 = float(input("Enter the first number: "))
                num2 = float(input("Enter the second number: "))
                
                if choice == 1:
                    print(f"Result: {add(num1, num2)}")
                elif choice == 2:
                    print(f"Result: {subtract(num1, num2)}")
                elif choice == 3:
                    print(f"Result: {multiply(num1, num2)}")
                elif choice == 4:
                    print(f"Result: {divide(num1, num2)}")
                elif choice == 5:
                    print(f"Result: {exponentiate(num1, num2)}")
            
            elif choice == 6:  # Square root
                num = float(input("Enter the number: "))
                print(f"Result: {square_root(num)}")
            
            elif choice in [7, 8, 9]:  # Trigonometric operations
                angle = float(input("Enter the angle in degrees: "))
                if choice == 7:
                    print(f"Result: {sine(angle)}")
                elif choice == 8:
                    print(f"Result: {cosine(angle)}")
                elif choice == 9:
                    print(f"Result: {tangent(angle)}")
            
            else:
                print("Invalid choice! Please select a valid operation.")
        
        except CalculatorError as ce:
            print(f"Error: {ce}")
        except ValueError:
            print("Error: Invalid input! Please enter numbers only.")
        except Exception as e:
            print(f"Unexpected error: {e}")


calculator()
