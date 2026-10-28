# 1. Count digits and calculate their sum
def count_digits_and_sum():
    text = input("Enter a string: ")
    # TODO: Count the digits and find their sum.
    # Hint: isdigit() - checks if a character is a digit
    count = 0
    sum = 0
    for i in text:
        if i.isdigit():
            count += 1
            sum += int(i)
    print("Count:", count)
    print("Sum:", sum)


# 2. Reverse a string and check whether it is a palindrome
def reverse_and_check_palindrome():
    text = input("Enter a string: ")
    # TODO: Reverse the string with slicing, then check if it matches the original.
    # Hint: [start:stop:step] slices a string; a step of -1 reverses it

    reversed_text = text[::-1]
    print ("Reversed text:", reversed_text)

    if text == reversed_text:
        print("It's a palindrome")
    else:
        print("Not true palindrome")
    



# 3. Print the initials of a three-part name
def print_initials():
    full_name = input("Enter your full name: ")
    # TODO: Split the name into three parts and print the initials.
    # Hint: split() - separates a string into words
    name= full_name.split()

    first_name= name[0][0]
    middle_name= name[1][0]
    last_initial= name[2][0]

    print(f"Initials: {first_name}.{middle_name}.{last_initial}")


# 4. Remove surrounding spaces and replace "Python" with "Caffeine"
def replace_word_and_trim_spaces():
    sentence = input("Enter a sentence: ")
    # TODO: Trim the ends, replace "Python" with "Caffeine", and print the result.
    # Hint: strip() - removes spaces at the ends
    # Hint: replace() - substitutes text
    new_sentence = sentence.strip()
    new_sentence = new_sentence.replace("Python", "Caffeine")

    print("Modified Sentence:", new_sentence)


# 5. Search for a string and report whether/how often it occurs
def search_string():
    sentence = input("Enter a sentence: ")
    search = input("Enter a search string: ")
    # TODO: Print whether it was found, its first position, and how many times it occurs.
    # Hint: in - checks whether text is present
    # Hint: find() - gets its first position
    # Hint: count() - counts how many times it appears
    found= search in sentence
    find_search = sentence.find(search)
    count = sentence.count(search)

    if found:
        print("Found:", found)
        print("First position:", find_search)
        print("Count:", count)
    else:
        print("Not found)")


def main():
    count_digits_and_sum()
    reverse_and_check_palindrome()
    print_initials()
    replace_word_and_trim_spaces()
    search_string()


if __name__ == "__main__":
    main()
