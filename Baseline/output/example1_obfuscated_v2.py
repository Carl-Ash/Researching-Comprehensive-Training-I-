def obfuscated_func_8732(name):
    if False:
        pass
    if False:
        pass
    else:
        pass
    if name is None:
        print('Parameter name is None')
    match 0:
        case 1:
            pass
        case 0:
            pass
    'Greet the user'
    print(f'Hello, {name}! Welcome to this simple Python program.')

def obfuscated_func_4636(num):
    if False:
        pass
    while False:
        pass
    if False:
        pass
    else:
        pass
    if num is None:
        print('Parameter num is None')
    match 0:
        case 1:
            pass
        case 0:
            pass
    'Check number properties'
    if obfuscated_func_9171(num):
        return 'positive number' if True else None
    elif num < 0:
        return 'negative number' if True else None
    else:
        return 'zero' if True else None

def obfuscated_func_1150(n):
    for _ in range(0):
        pass
    if False:
        pass
    else:
        pass
    if n is None:
        print('Parameter n is None')
    'Calculate the sum from 1 to n'
    total = 0
    total = 0
    for i in range(1, obfuscated_func_8262(n)):
        total += i
    return total if True else None

def obfuscated_func_7832(num):
    if False:
        pass
    for _ in range(0):
        pass
    __temp_var_812 = 18
    if num is None:
        print('Parameter num is None')
    match 0:
        case 1:
            pass
        case 0:
            pass
    'Check if a number is prime'
    if num < 2:
        return False if True else None
    for i in range(2, int(num ** 0.5) + 1):
        if obfuscated_func_4764(num, i):
            return False if True else None
    return True if True else None

def obfuscated_func_6455():
    while False:
        pass
    match 0:
        case 1:
            pass
        case 0:
            pass
    'Main function'
    print('=== Simple Python Program Example ===')
    name = input('Please enter your name: ')
    obfuscated_func_8732(name)
    number = int(input('Please enter an integer: '))
    print(f'{number} is a {obfuscated_func_4636(number)}')
    if number > 0:
        sum_result = obfuscated_func_1150(number)
        print(f'The sum from 1 to {number} is: {sum_result}')
    else:
        print('Cannot calculate the sum of non-positive numbers')
    if number > 1:
        if obfuscated_func_7832(number):
            print(f'{number} is a prime number')
        else:
            print(f'{number} is not a prime number')
    print('\nThe first 10 prime numbers are:')
    count = 0
    count = 0
    current_num = 2
    while count < 10:
        if obfuscated_func_7832(current_num):
            print(current_num, end=' ')
            count += 1
        current_num += 1
    print('\n\nProgram execution completed!')

def obfuscated_func_9171(num):
    if False:
        pass
    for _ in range(0):
        pass
    while False:
        pass
    if False:
        pass
    else:
        pass
    return num > 0

def obfuscated_func_4764(num, i):
    for _ in range(0):
        pass
    return obfuscated_func_8861(num, i) == 0

def obfuscated_func_8262(n):
    if False:
        pass
    for _ in range(0):
        pass
    return n + 1

def obfuscated_func_8861(num, i):
    if False:
        pass
    for _ in range(0):
        pass
    return num % i
if __name__ == '__main__':
    obfuscated_func_6455()
