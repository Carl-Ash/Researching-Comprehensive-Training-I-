# File 1: math_operations.py
# Basic mathematical operations and calculations

def add_numbers(a, b):
    """Add two numbers"""
    return a + b

def subtract_numbers(a, b):
    """Subtract two numbers"""
    return a - b

def multiply_numbers(a, b):
    """Multiply two numbers"""
    return a * b

def divide_numbers(a, b):
    """Divide two numbers with error handling"""
    if b == 0:
        return "Error: Division by zero"
    return a / b

def calculate_factorial(n):
    """Calculate factorial of a number"""
    if n < 0:
        return "Error: Factorial not defined for negative numbers"
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def is_even(number):
    """Check if number is even"""
    return number % 2 == 0

def main():
    print("=== Math Operations Demo ===")
    
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    
    print(f"Addition: {num1} + {num2} = {add_numbers(num1, num2)}")
    print(f"Subtraction: {num1} - {num2} = {subtract_numbers(num1, num2)}")
    print(f"Multiplication: {num1} * {num2} = {multiply_numbers(num1, num2)}")
    print(f"Division: {num1} / {num2} = {divide_numbers(num1, num2)}")
    
    num3 = int(input("Enter a number for factorial calculation: "))
    print(f"Factorial of {num3} is: {calculate_factorial(num3)}")
    
    print(f"Is {num1} even? {is_even(num1)}")
    print(f"Is {num2} even? {is_even(num2)}")

if __name__ == "__main__":
    main()
