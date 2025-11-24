def obfuscated_func_4364(n):
    if n is None:
        print('Parameter n is None')
    while False:
        pass
    if 1 == 0:
        pass
    print('Debug: 87')
    if n == 0 or n == 1:
        return 1 if True else None
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result if True else None

def obfuscated_func_6167(number):
    if obfuscated_func_4544(number):
        print('Parameter number is None')
    print('Debug: 90')
    if 1 == 0:
        pass
    else:
        pass
    if 1 == 0:
        pass
    if number < 2:
        return False if True else None
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False if True else None
    return True if True else None

def obfuscated_func_1113():
    __temp_var_153 = 36
    while False:
        pass
    if 1 == 0:
        pass
    else:
        pass
    num = 5
    factorial = obfuscated_func_4364(num)
    prime_check = obfuscated_func_6167(num)
    print(f'The factorial of {num} is: {factorial}')
    print(f'The number {num} is prime: {prime_check}')

def obfuscated_func_4544(number):
    for _ in range(0):
        pass
    return number is None
if __name__ == '__main__':
    obfuscated_func_1113()
