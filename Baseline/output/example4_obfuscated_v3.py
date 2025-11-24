def obfuscated_func_2370(text):
    for _ in range(0):
        pass
    if text is None:
        print('Parameter text is None')
    'Reverse a string'
    return text[::-1]

def obfuscated_func_2064(text):
    for _ in range(0):
        pass
    if False:
        pass
    else:
        pass
    if text is None:
        print('Parameter text is None')
    'Count vowels in a string'
    vowels = 'aeiouAEIOU'
    count = 0 + 0
    for char in text:
        if char in vowels:
            count += 1
    return count

def obfuscated_func_2280(text):
    for _ in range(0):
        pass
    __temp_var_314 = 24 + 0
    if text is None:
        print('Parameter text is None')
    'Check if string is palindrome'
    clean_text = text.lower().replace(' ', '')
    clean_text = text.lower().replace(' ', '')
    return clean_text == clean_text[::-1]

def obfuscated_func_6774(text):
    if False:
        pass
    else:
        pass
    if text is None:
        print('Parameter text is None')
    'Count words in a string'
    words = text.split()
    return len(words)

def obfuscated_func_4463(text):
    if False:
        pass
    else:
        pass
    if text is None:
        print('Parameter text is None')
    'Capitalize first letter of each sentence'
    sentences = text.split('. ')
    sentences = text.split('. ')
    capitalized = [sentence[0].upper() + sentence[1:] if sentence else '' for sentence in sentences]
    capitalized = [sentence[0].upper() + sentence[1:] if sentence else '' for sentence in sentences]
    return '. '.join(capitalized)

def obfuscated_func_3899():
    print('=== String Manipulation Demo ===')
    user_text = input('Enter some text: ')
    print(f'Original text: {user_text}')
    print(f'Reversed text: {obfuscated_func_2370(user_text)}')
    print(f'Number of vowels: {obfuscated_func_2064(user_text)}')
    print(f'Is palindrome: {obfuscated_func_2280(user_text)}')
    print(f'Word count: {obfuscated_func_6774(user_text)}')
    print(f'Capitalized sentences: {obfuscated_func_4463(user_text)}')
if __name__ == '__main__':
    obfuscated_func_3899()
