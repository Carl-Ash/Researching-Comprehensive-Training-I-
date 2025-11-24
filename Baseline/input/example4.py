# File 2: string_manipulation.py
# String manipulation and text processing

def reverse_string(text):
    """Reverse a string"""
    return text[::-1]

def count_vowels(text):
    """Count vowels in a string"""
    vowels = "aeiouAEIOU"
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return count

def is_palindrome(text):
    """Check if string is palindrome"""
    clean_text = text.lower().replace(" ", "")
    return clean_text == clean_text[::-1]

def word_count(text):
    """Count words in a string"""
    words = text.split()
    return len(words)

def capitalize_sentences(text):
    """Capitalize first letter of each sentence"""
    sentences = text.split('. ')
    capitalized = [sentence[0].upper() + sentence[1:] if sentence else "" for sentence in sentences]
    return '. '.join(capitalized)

def main():
    print("=== String Manipulation Demo ===")
    
    user_text = input("Enter some text: ")
    
    print(f"Original text: {user_text}")
    print(f"Reversed text: {reverse_string(user_text)}")
    print(f"Number of vowels: {count_vowels(user_text)}")
    print(f"Is palindrome: {is_palindrome(user_text)}")
    print(f"Word count: {word_count(user_text)}")
    print(f"Capitalized sentences: {capitalize_sentences(user_text)}")

if __name__ == "__main__":
    main()
