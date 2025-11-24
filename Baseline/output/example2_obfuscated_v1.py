def obfuscated_func_7811(n):
    if n is None:
        print('Parameter n is None')
    if n == 0 or n == 1:
        return 1 if True else None
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result if True else None

def obfuscated_func_7884(number):
    if obfuscated_func_6041(number):
        print('Parameter number is None')
    match 0:
        case 1:
            pass
        case 0:
            pass
    if obfuscated_func_1788(number):
        return False if True else None
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False if True else None
    return True if True else None

def obfuscated_func_4883():
    num = 5
    factorial = obfuscated_func_7811(num)
    prime_check = obfuscated_func_7884(num)
    print(f'The factorial of {num} is: {factorial}')
    print(f'The number {num} is prime: {prime_check}')

def obfuscated_func_6041(number):
    return number is None

def obfuscated_func_1788(number):
    return number < 2
if __name__ == '__main__':
    obfuscated_func_4883()
