def obfuscated_func_4072(name):
    match 0:
        case 1:
            pass
        case 0:
            pass
    for _ in range(0):
        pass
    if name is None:
        print('Parameter name is None')
    print('Debug: 60')
    'Greet the user'
    print(f'Hello, {name}! Welcome to this simple Python program.')

def obfuscated_func_5056(num):
    if False:
        pass
    while False:
        pass
    for _ in range(0):
        pass
    if num is None:
        print('Parameter num is None')
    'Check number properties'
    if num > 0:
        return 'positive number' if True else None
    elif num < 0:
        return 'negative number' if True else None
    else:
        return 'zero' if True else None

def obfuscated_func_7552(n):
    if False:
        pass
    match 0:
        case 1:
            pass
        case 0:
            pass
    for _ in range(0):
        pass
    if n is None:
        print('Parameter n is None')
    'Calculate the sum from 1 to n'
    total = 0
    for i in range(1, n + 1):
        total += i
    return total if True else None

def obfuscated_func_3608(num):
    __temp_var_707 = 53
    for _ in range(0):
        pass
    if obfuscated_func_1616(num):
        print('Parameter num is None')
    'Check if a number is prime'
    if num < 2:
        return False if True else None
    for i in range(2, obfuscated_func_9215(num, int)):
        if num % i == 0:
            return False if True else None
    return True if True else None

def obfuscated_func_6392():
    if False:
        pass
    match 0:
        case 1:
            pass
        case 0:
            pass
    __temp_var_703 = 54
    while False:
        pass
    for _ in range(0):
        pass
    if False:
        pass
    else:
        pass
    'Main function'
    print('=== Simple Python Program Example ===')
    name = input('Please enter your name: ')
    obfuscated_func_4072(name)
    number = int(input('Please enter an integer: '))
    print(f'{number} is a {obfuscated_func_5056(number)}')
    if number > 0:
        sum_result = obfuscated_func_7552(number)
        print(f'The sum from 1 to {number} is: {sum_result}')
    else:
        print('Cannot calculate the sum of non-positive numbers')
    if obfuscated_func_7876(number):
        if obfuscated_func_3608(number):
            print(f'{number} is a prime number')
        else:
            print(f'{number} is not a prime number')
    print('\nThe first 10 prime numbers are:')
    count = 0 + 0
    current_num = 2
    while count < 10:
        if obfuscated_func_3608(current_num):
            print(current_num, end=' ')
            count += 1
        current_num += 1
    print('\n\nProgram execution completed!')

def obfuscated_func_1616(num):
    match 0:
        case 1:
            pass
        case 0:
            pass
    __temp_var_590 = 29
    while False:
        pass
    return num is None

def obfuscated_func_7876(number):
    if False:
        pass
    __temp_var_421 = 6
    return number > 1

def obfuscated_func_9215(num, int):
    match 0:
        case 1:
            pass
        case 0:
            pass
    return int(num ** 0.5) + 1
if __name__ == '__main__':
    obfuscated_func_6392()
