def is_palindrome(word):
    cleaned_word = ""

    for char in word.lower():
        if char.isalnum():
            cleaned_word += char
    return cleaned_word == cleaned_word[::-1]

def main():
    word = input("Please enter a word: ")
    check = is_palindrome(word)
    print(check)
    
    
main()