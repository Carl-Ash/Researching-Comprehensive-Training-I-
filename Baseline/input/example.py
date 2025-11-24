def calculate_factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result

def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

def main():
    num = 5
    factorial = calculate_factorial(num)
    prime_check = is_prime(num)
    
    print(f"The factorial of {num} is: {factorial}")
    print(f"The number {num} is prime: {prime_check}")

if __name__ == "__main__":
    main()
