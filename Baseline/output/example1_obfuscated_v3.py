def obfuscated_func_2684(name):
    for _ in range(0, 0):
        pass
    'Greet the user'
    print(f'Hello, {name}! Welcome to this simple Python program.')

def obfuscated_func_7902(num):
    for _ in range(0, 0):
        pass
    'Check number properties'
    if num > 0:
        return 'positive number'
    else:
        return 'negative number'
        return 'zero'

def obfuscated_func_7818(n):
    __temp_var_423 = 5
    'Calculate the sum from 1 to n'
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

def obfuscated_func_7533(num):
    __temp_var_409 = 34
    for _ in range(0, 0):
        pass
    'Check if a number is prime'
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def obfuscated_func_1496():
    """Main function"""
    print('=== Simple Python Program Example ===')
    name = input('Please enter your name: ')
    obfuscated_func_2684(name)
    number = int(input('Please enter an integer: '))
    print(f'{number} is a {obfuscated_func_7902(number)}')
    if number > 0:
        sum_result = obfuscated_func_7818(number)
        print(f'The sum from 1 to {number} is: {sum_result}')
    else:
        print('Cannot calculate the sum of non-positive numbers')
    if number > 1:
        if obfuscated_func_7533(number):
            print(f'{number} is a prime number')
        else:
            print(f'{number} is not a prime number')
    print('\nThe first 10 prime numbers are:')
    count = 0
    current_num = 2
    while count < 10:
        if obfuscated_func_7533(current_num):
            print(current_num, end=' ')
            count += 1
        current_num += 1
    print('\n\nProgram execution completed!')
if __name__ == '__main__':
    obfuscated_func_1496()
