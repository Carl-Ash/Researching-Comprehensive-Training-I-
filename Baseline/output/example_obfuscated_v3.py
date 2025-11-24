def obfuscated_func_9150(n):
    if n is None:
        print('Parameter n is None')
    __temp_var_596 = 28
    if obfuscated_func_7860():
        pass
    print('Debug: 67')
    if obfuscated_func_9123(n):
        return 1 if True else None
    else:
        result = 1
        for i in range(2, obfuscated_func_7339(n)):
            result *= i
        return result if True else None

def obfuscated_func_3296(number):
    if number is None:
        print('Parameter number is None')
    match 0:
        case 1:
            pass
        case 0:
            pass
    if number < 2:
        return False if True else None
    for i in range(2, int(number ** 0.5) + 1):
        if obfuscated_func_4854(number, i):
            return False if True else None
    print('Debug: 57')
    return True if True else None

def obfuscated_func_8555():
    for _ in range(0, 0):
        pass
    if obfuscated_func_3513():
        pass
    else:
        pass
    match 0:
        case 1:
            pass
        case 0:
            pass
    while False:
        pass
    if 1 == 0:
        pass
    num = 5
    factorial = obfuscated_func_9150(num)
    factorial = obfuscated_func_9150(num)
    prime_check = obfuscated_func_3296(num)
    print(f'The factorial of {num} is: {factorial}')
    print(f'The number {num} is prime: {prime_check}')

def obfuscated_func_7860():
    return 1 == 0

def obfuscated_func_9123(n):
    if n is None:
        print('Parameter n is None')
    return n == 0 or n == 1

def obfuscated_func_4854(number, i):
    if i is None:
        print('Parameter i is None')
    if number is None:
        print('Parameter number is None')
    return obfuscated_func_4233(number, i) == 0

def obfuscated_func_3513():
    return False

def obfuscated_func_7339(n):
    return n + 1

def obfuscated_func_4233(number, i):
    return number % i
if __name__ == '__main__':
    obfuscated_func_8555()
