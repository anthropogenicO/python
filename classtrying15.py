def summarize_letters(st1):
    st1 = st1.lower()
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    result = []

    for letter in st1:
        if letter in alphabet:
            frequency = st1.count(letter)
            item = (letter, frequency)

            if item not in result:
                result.append(item)

    return result


def main():
    st1 = "astwqswa"
    result = summarize_letters(st1)

    print(result)

    for letter, frequency in result:
        print(letter, ":", frequency)

    if len(result) == 26:
        print("The string has all the letters of the alphabet.")
    else:
        print("The string does not have all the letters of the alphabet.")


main()