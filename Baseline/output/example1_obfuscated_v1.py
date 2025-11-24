def obfuscated_func_5928(name):
    __temp_var_427 = 67
    'Greet the user'
    print(f'Hello, {name}! Welcome to this simple Python program.')

def obfuscated_func_1819(num):
    __temp_var_444 = 4
    if 1 == 0:
        pass
    else:
        pass
    'Check number properties'
    if num > 0:
        return 'positive number'
    else:
        return 'negative number'
        return 'zero'

def obfuscated_func_8678(n):
    while False:
        pass
    'Calculate the sum from 1 to n'
    total = 0
    for i in range(1, obfuscated_func_1016(n)):
        total += i
    return total

def obfuscated_func_1672(num):
    while False:
        pass
    'Check if a number is prime'
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def obfuscated_func_3296():
    __temp_var_814 = 76
    'Main function'
    print('=== Simple Python Program Example ===')
    name = input('Please enter your name: ')
    obfuscated_func_5928(name)
    number = int(input('Please enter an integer: '))
    print(f'{number} is a {obfuscated_func_1819(number)}')
    if number > 0:
        sum_result = obfuscated_func_8678(number)
        print(f'The sum from 1 to {number} is: {sum_result}')
    else:
        print('Cannot calculate the sum of non-positive numbers')
    if number > 1:
        if obfuscated_func_1672(number):
            print(f'{number} is a prime number')
        else:
            print(f'{number} is not a prime number')
    print('\nThe first 10 prime numbers are:')
    count = 0
    current_num = 2
    while count < 10:
        if obfuscated_func_1672(current_num):
            print(current_num, end=' ')
            count += 1
        current_num += 1
    print('\n\nProgram execution completed!')

def obfuscated_func_1016(n):
    return n + 1
if __name__ == '__main__':
    obfuscated_func_3296()
