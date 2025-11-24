# Simple Python program example
def greet_user(name):
    """Greet the user"""
    print(f"Hello, {name}! Welcome to this simple Python program.")

def check_number(num):
    """Check number properties"""
    if num > 0:
        return "positive number"
    elif num < 0:
        return "negative number"
    else:
        return "zero"

def calculate_sum(n):
    """Calculate the sum from 1 to n"""
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

def is_prime(num):
    """Check if a number is prime"""
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def main():
    """Main function"""
    print("=== Simple Python Program Example ===")
    
    # Get user input
    name = input("Please enter your name: ")
    greet_user(name)
    
    # Number check
    number = int(input("Please enter an integer: "))
    print(f"{number} is a {check_number(number)}")
    
    # Calculate cumulative sum
    if number > 0:
        sum_result = calculate_sum(number)
        print(f"The sum from 1 to {number} is: {sum_result}")
    else:
        print("Cannot calculate the sum of non-positive numbers")
    
    # Prime number check
    if number > 1:
        if is_prime(number):
            print(f"{number} is a prime number")
        else:
            print(f"{number} is not a prime number")
    
    # Display some prime numbers
    print("\nThe first 10 prime numbers are:")
    count = 0
    current_num = 2
    while count < 10:
        if is_prime(current_num):
            print(current_num, end=" ")
            count += 1
        current_num += 1
    
    print("\n\nProgram execution completed!")

# Run main function
if __name__ == "__main__":
    main()
