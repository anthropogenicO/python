def get_word_details(word):
    """Return the length, first character, and last character of a non-empty word."""
    # TODO: Find the word's length, first character, and last character.
    # TODO: Return all three values.
    word_length = len(word)
    first_char= word[0]
    last_char= word[-1]

    return word_length, first_char, last_char


def create_character_list(word):
    """Build and return a character list using append()."""
    # TODO: Create an empty list.
    # TODO: Add each character from word to the list using append().
    # TODO: Return the list.
    characters = []
    for character in word:
        characters.append(character)
    return characters



def filter_english_letters(sentence, alphabet):
    """Return lowercase English letters found in a sentence using in."""
    # TODO: Convert the sentence to lowercase.
    # TODO: Keep only characters that are in alphabet.
    # TODO: Return the list of letters and the joined string.
    sentence = sentence.lower()
    compressed_list = []

    for char in sentence:
        if char in alphabet:
            compressed_list.append(char)
    compressed_string = "".join(compressed_list)
    return compressed_list, compressed_string



def count_letter_frequencies(text, alphabet):
    """Count each English letter and return the frequency list."""
    # TODO: create the frequency list.
    # TODO: Convert text to lowercase.
    # TODO: Count each character found in alphabet.
    # TODO: Return the updated frequency list.
    frequencies = [0]* len(alphabet)
    for char in text:
        if char in alphabet:
            postion = alphabet.index(char)
            frequencies[postion] += 1
    return frequencies


def main():
    alphabet = list("abcdefghijklmnopqrstuvwxyz")

    # Exercise 1
    word = input("1.Enter a non-empty word: ")
    word_length, first_char, last_char = get_word_details(word)
    print(f"Number of characters: {word_length}")
    print(f"First character: {first_char}")
    print(f"Last character: {last_char}")
    print()

    # Exercise 2
    word = input("2.Enter a word: ")
    characters = create_character_list(word)
    print(characters)
    for character in characters:
        print(character)
    print()

    # Exercise 3
    sentence = input("3.Enter a sentence: ")
    compressed_list, compressed_string = filter_english_letters(sentence, alphabet)
    print(compressed_list)
    print(compressed_string)
    print()

    # Exercise 4
    text = input("4.Enter a word: ")
    # TODO: call count_letter_frequencies(), and print the frequency chart.
    frequencies = count_letter_frequencies(text, alphabet)
    for index in range(len(alphabet)):
        print(alphabet[index], "*"* frequencies[index])


if __name__ == "__main__":
    main()