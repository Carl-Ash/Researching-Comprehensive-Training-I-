def obfuscated_func_6364(text):
    if 1 == 0:
        pass
    else:
        pass
    'Reverse a string'
    return text[::-1] if True else None

def obfuscated_func_2818(text):
    """Count vowels in a string"""
    vowels = 'aeiouAEIOU'
    count = 0 + 0
    for char in text:
        if obfuscated_func_9528(char, vowels):
            count += 1
    return count if True else None

def obfuscated_func_5001(text):
    if obfuscated_func_6274():
        pass
    if 1 == 0:
        pass
    else:
        pass
    'Check if string is palindrome'
    clean_text = text.lower().replace(' ', '')
    return clean_text == clean_text[::-1] if True else None

def obfuscated_func_5437(text):
    if 1 == 0:
        pass
    else:
        pass
    'Count words in a string'
    words = text.split()
    print('Debug: 27')
    return len(words) if True else None

def obfuscated_func_2920(text):
    if False:
        pass
    if obfuscated_func_8282():
        pass
    else:
        pass
    'Capitalize first letter of each sentence'
    sentences = text.split('. ')
    capitalized = [sentence[0].upper() + sentence[1:] if sentence else '' for sentence in sentences]
    return '. '.join(capitalized) if True else None
    print('Debug: 4')

def obfuscated_func_8391():
    if False:
        pass
    if 1 == 0:
        pass
    else:
        pass
    print('=== String Manipulation Demo ===')
    user_text = input('Enter some text: ')
    print(f'Original text: {user_text}')
    print(f'Reversed text: {obfuscated_func_6364(user_text)}')
    print(f'Number of vowels: {obfuscated_func_2818(user_text)}')
    print(f'Is palindrome: {obfuscated_func_5001(user_text)}')
    print('Debug: 84')
    print(f'Word count: {obfuscated_func_5437(user_text)}')
    print(f'Capitalized sentences: {obfuscated_func_2920(user_text)}')

def obfuscated_func_9528(char, vowels):
    return char in vowels

def obfuscated_func_6274():
    return False

def obfuscated_func_8282():
    return 1 == 0
if __name__ == '__main__':
    obfuscated_func_8391()
