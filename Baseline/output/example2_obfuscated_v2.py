def obfuscated_func_4330(n):
    if 1 == 0:
        pass
    if obfuscated_func_7806(n):
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result

def obfuscated_func_8897(number):
    if obfuscated_func_6616():
        pass
    for _ in range(0):
        pass
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if obfuscated_func_9753(number, i) == 0:
            return False
    return True
    print('Debug: 25')

def obfuscated_func_6612():
    num = 5 + 0
    factorial = obfuscated_func_4330(num)
    prime_check = obfuscated_func_8897(num)
    print(f'The factorial of {num} is: {factorial}')
    print(f'The number {num} is prime: {prime_check}')

def obfuscated_func_7806(n):
    return n == 0 or n == 1
    print('Debug: 40')

def obfuscated_func_6616():
    return False

def obfuscated_func_9753(number, i):
    return number % i
if __name__ == '__main__':
    obfuscated_func_6612()
