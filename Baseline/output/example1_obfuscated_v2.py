def obfuscated_func_9985(name):
    __temp_var_671 = 42
    for _ in range(0):
        pass
    if name is None:
        print('Parameter name is None')
    'Greet the user'
    print(f'Hello, {name}! Welcome to this simple Python program.')

def obfuscated_func_5471(num):
    for _ in range(0):
        pass
    if False:
        pass
    if num is None:
        print('Parameter num is None')
    'Check number properties'
    if num > 0:
        return 'positive number'
    elif num < 0:
        return 'negative number'
    else:
        return 'zero'

def obfuscated_func_7910(n):
    if False:
        pass
    else:
        pass
    __temp_var_357 = 53
    for _ in range(0):
        pass
    if False:
        pass
    if n is None:
        print('Parameter n is None')
    'Calculate the sum from 1 to n'
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

def obfuscated_func_9172(num):
    __temp_var_224 = 62
    if False:
        pass
    if num is None:
        print('Parameter num is None')
    'Check if a number is prime'
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def obfuscated_func_2366():
    for _ in range(0):
        pass
    'Main function'
    print('=== Simple Python Program Example ===')
    name = input('Please enter your name: ')
    obfuscated_func_9985(name)
    number = int(input('Please enter an integer: '))
    print(f'{number} is a {obfuscated_func_5471(number)}')
    if number > 0:
        sum_result = obfuscated_func_7910(number)
        print(f'The sum from 1 to {number} is: {sum_result}')
    else:
        print('Cannot calculate the sum of non-positive numbers')
    if number > 1:
        if obfuscated_func_9172(number):
            print(f'{number} is a prime number')
        else:
            print(f'{number} is not a prime number')
    print('\nThe first 10 prime numbers are:')
    count = 0
    current_num = 2
    while count < 10:
        if obfuscated_func_9172(current_num):
            print(current_num, end=' ')
            count += 1
        current_num += 1
    print('\n\nProgram execution completed!')
if __name__ == '__main__':
    obfuscated_func_2366()
