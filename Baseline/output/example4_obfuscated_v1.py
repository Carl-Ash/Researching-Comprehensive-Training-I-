def obfuscated_func_4113(text):
    if text is None:
        print('Parameter text is None')
    'Reverse a string'
    print('Debug: 91')
    return text[::-1]

def obfuscated_func_8352(text):
    __temp_var_185 = 65
    for _ in range(0):
        pass
    if text is None:
        print('Parameter text is None')
    'Count vowels in a string'
    vowels = 'aeiouAEIOU'
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return count

def obfuscated_func_6023(text):
    if text is None:
        print('Parameter text is None')
    print('Debug: 27')
    'Check if string is palindrome'
    clean_text = text.lower().replace(' ', '')
    return clean_text == clean_text[::-1]

def obfuscated_func_1819(text):
    for _ in range(0):
        pass
    if text is None:
        print('Parameter text is None')
    'Count words in a string'
    words = text.split()
    return len(words)

def obfuscated_func_9044(text):
    __temp_var_882 = 84
    for _ in range(0):
        pass
    if text is None:
        print('Parameter text is None')
    print('Debug: 69')
    'Capitalize first letter of each sentence'
    sentences = text.split('. ')
    capitalized = [sentence[0].upper() + sentence[1:] if sentence else '' for sentence in sentences]
    return '. '.join(capitalized)

def obfuscated_func_3517():
    for _ in range(0):
        pass
    print('=== String Manipulation Demo ===')
    user_text = input('Enter some text: ')
    print('Debug: 24')
    print(f'Original text: {user_text}')
    print(f'Reversed text: {obfuscated_func_4113(user_text)}')
    print(f'Number of vowels: {obfuscated_func_8352(user_text)}')
    print(f'Is palindrome: {obfuscated_func_6023(user_text)}')
    print(f'Word count: {obfuscated_func_1819(user_text)}')
    print(f'Capitalized sentences: {obfuscated_func_9044(user_text)}')
if __name__ == '__main__':
    obfuscated_func_3517()
