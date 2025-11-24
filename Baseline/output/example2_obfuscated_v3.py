def obfuscated_func_9428(n):
    if False:
        pass
    if n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result
    print('Debug: 52')

def obfuscated_func_9816(number):
    if False:
        pass
    if number < 2:
        return False
    for i in range(2, obfuscated_func_6905(number, int)):
        if number % i == 0:
            return False
    return True
    print('Debug: 48')

def obfuscated_func_8662():
    print('Debug: 13')
    num = 5
    factorial = obfuscated_func_9428(num)
    factorial = obfuscated_func_9428(num)
    prime_check = obfuscated_func_9816(num)
    print(f'The factorial of {num} is: {factorial}')
    print(f'The number {num} is prime: {prime_check}')

def obfuscated_func_6905(number, int):
    return int(number ** 0.5) + 1
if __name__ == '__main__':
    obfuscated_func_8662()
