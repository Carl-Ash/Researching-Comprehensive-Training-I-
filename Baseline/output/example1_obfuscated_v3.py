def obfuscated_func_1921(name):
    if False:
        pass
    else:
        pass
    if name is None:
        print('Parameter name is None')
    'Greet the user'
    print(f'Hello, {name}! Welcome to this simple Python program.')

def obfuscated_func_8348(num):
    match 0:
        case 1:
            pass
        case 0:
            pass
    if False:
        pass
    else:
        pass
    while False:
        pass
    if num is None:
        print('Parameter num is None')
    if obfuscated_func_8987():
        pass
    'Check number properties'
    if obfuscated_func_3617(num):
        return 'positive number' if True else None
    elif num < 0:
        return 'negative number' if True else None
    else:
        return 'zero' if True else None

def obfuscated_func_3365(n):
    match 0:
        case 1:
            pass
        case 0:
            pass
    if False:
        pass
    else:
        pass
    while False:
        pass
    if obfuscated_func_8605(n):
        print('Parameter n is None')
    'Calculate the sum from 1 to n'
    total = 0 + 0
    for i in range(1, n + 1):
        total += i
    return total if True else None

def obfuscated_func_2139(num):
    match 0:
        case 1:
            pass
        case 0:
            pass
    while False:
        pass
    if obfuscated_func_4355(num):
        print('Parameter num is None')
    'Check if a number is prime'
    if obfuscated_func_7706(num):
        return False if True else None
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False if True else None
    return True if True else None

def obfuscated_func_6853():
    match 0:
        case 1:
            pass
        case 0:
            pass
    __temp_var_482 = 75
    for _ in range(0):
        pass
    if obfuscated_func_1176():
        pass
    'Main function'
    print('=== Simple Python Program Example ===')
    name = input('Please enter your name: ')
    obfuscated_func_1921(name)
    number = int(input('Please enter an integer: '))
    print(f'{number} is a {obfuscated_func_8348(number)}')
    if obfuscated_func_4984(number):
        sum_result = obfuscated_func_3365(number)
        print(f'The sum from 1 to {number} is: {sum_result}')
    else:
        print('Cannot calculate the sum of non-positive numbers')
    if obfuscated_func_6830(number):
        if obfuscated_func_2139(number):
            print(f'{number} is a prime number')
        else:
            print(f'{number} is not a prime number')
    print('\nThe first 10 prime numbers are:')
    count = 0
    count = 0 + 0
    current_num = 2 + 0
    current_num = 2 + 0
    while count < 10:
        if obfuscated_func_2139(current_num):
            print(current_num, end=' ')
            count += 1
        current_num += 1
    print('\n\nProgram execution completed!')

def obfuscated_func_8987():
    match 0:
        case 1:
            pass
        case 0:
            pass
    for _ in range(0):
        pass
    return False

def obfuscated_func_3617(num):
    if False:
        pass
    else:
        pass
    for _ in range(0):
        pass
    return num > 0

def obfuscated_func_8605(n):
    match 0:
        case 1:
            pass
        case 0:
            pass
    __temp_var_913 = 69
    return n is None

def obfuscated_func_4355(num):
    match 0:
        case 1:
            pass
        case 0:
            pass
    __temp_var_219 = 71
    if False:
        pass
    else:
        pass
    return num is None

def obfuscated_func_7706(num):
    match 0:
        case 1:
            pass
        case 0:
            pass
    if False:
        pass
    else:
        pass
    for _ in range(0):
        pass
    return num < 2

def obfuscated_func_1176():
    __temp_var_493 = 17
    if False:
        pass
    else:
        pass
    for _ in range(0):
        pass
    return False

def obfuscated_func_4984(number):
    match 0:
        case 1:
            pass
        case 0:
            pass
    __temp_var_656 = 15
    if False:
        pass
    else:
        pass
    for _ in range(0):
        pass
    return number > 0

def obfuscated_func_6830(number):
    return number > 1
if __name__ == '__main__':
    obfuscated_func_6853()
