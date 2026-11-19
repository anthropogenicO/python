# Project No.: 5
# Author: Mridul Hasan
# Description: Combibing strings, check their letters for a palindrome and display the frequency of each letter with stars.

from testModule import check_palindrome


# ask for the requested number of strings and combine them in the order entered
def user_string(number_of_strings):
    combined_string = ""
    for string_number in range(1, number_of_strings + 1):
        # Keep spaces and punctuation the user types in each string.
        combined_string += input(f"Enter string {string_number}: ")
    return combined_string


# Display the combined string before making any changes to itt
def show_string(combined_string):
    print(combined_string)


# make a lowercase copy so uppercase and lowercase letters are counted together.
def convert_string_lower(combined_string):
    return combined_string.lower()


# turn the lowercase string into a list containing one character per position.
def string_to_list(lowercase_string):
    character_list = list(lowercase_string)
    # Join the list when printing so the output matches the sample format.
    print("".join(character_list))
    return character_list


# Copy only the letters into a new list, leaving out spaces nd punctuation
def compress_list(character_list):
    compressed_list = []
    for character in character_list:
        # The frequency report uses the 26 letters from a through z.
        if "a" <= character <= "z":
            compressed_list.append(character)

    #display the compressed letters together as shown in the sample.
    print("".join(compressed_list))
    return compressed_list


#count each letter and store its count in the matching alphabet position.
def frequency_count(frequency_list, alphabet_list, compressed_list):
    for letter in compressed_list:
        for index in range(len(alphabet_list)):
            if letter == alphabet_list[index]:
                frequency_list[index] += 1
                #letter has been found, so move on to the next one.
                break
    return frequency_list


#print every alphabet letter and one star for each time it appears.
def show_frequency(frequency_list):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for index in range(len(frequency_list)):
        stars = "*" * frequency_list[index]
        # Put the stars in the same column for all 26 letters.
        print(f"{alphabet[index]:<2}{stars}")


#run the steps of the program in the order required by the project.
def main():
    #keep asking until the user enters a positive integer.
    number_of_strings = 0
    while number_of_strings <= 0:
        try:
            number_of_strings = int(input("Enter the number of strings you want to read: "))
        except ValueError:
            #words and decimal numbers cannot be used as the number of strings.
            number_of_strings = 0
        if number_of_strings <= 0:
            print("Please enter a positive integer.")

    # Show the original text, then make lowercase and compressed character lists.
    combined_string = user_string(number_of_strings)
    show_string(combined_string)

    lowercase_string = convert_string_lower(combined_string)
    character_list = string_to_list(lowercase_string)
    compressed_list = compress_list(character_list)

    # The palindrome test ignores spaces, punctuation, and letter case.
    if check_palindrome(compressed_list):
        print("These letters form a palindrome.")
    else:
        print("These letters do not form a palindrome.")

    # Start with 26 zero counts, one for each letter in the alphabet list.
    frequency_list = [0] * 26
    alphabet_list = list("abcdefghijklmnopqrstuvwxyz")
    frequency_list = frequency_count(frequency_list, alphabet_list, compressed_list)

    # Show the frequency report below the palindrome result.
    print()
    print("Following is the frequency distribution for the letters in the list.")
    print()
    show_frequency(frequency_list)


if __name__ == "__main__":
    main()
