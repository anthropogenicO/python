# CS 1110 - COMPUTER SCIENCE I LAB
# LAB EXERCISE: Sets and Dictionaries Practice

# QUESTION 1: Set Practice
def set_operations():
    # TODO:
    # 1. Create two sets:
    set_A = {1, 3, 5, 7, 9}
    set_B = {2, 3, 5, 7, 11}
    # 2. Print:
    #       - The union of both sets
    print("Union:", set_A | set_B)
    #       - The intersection
    #       - The difference (A - B)
    #       - The symmetric difference
    # HINT: use |, &, -, and ^ operators.
    print("Intersection:", set_A & set_B)
    print("Difference:", set_A - set_B)
    print("Symmetric Difference:", set_A ^ set_B)
    #       - The union of both sets
    #       - The intersection
    #       - The difference (A - B)
    #       - The symmetric difference
    # HINT: use |, &, -, and ^ operators.


# QUESTION 2: Dictionary Practice
def dictionary_practice():
    # TODO:
    book = {"title": "Python Basics", "price": 25.99}
    print(f"{book['title']} - ${book['price']}")
    print()

    book['year'] = 2024
    book['price'] = 19.99

    book2 = {
        'title': 'Learning Java',
        'price': 29.59,
        'year': 2023
    }

    library = [book, book2]

    for current_book in library:
        print(f"{current_book['title']} ({current_book['year']}) - ${current_book['price']}")
    # 1. Create a dictionary named 'book' with keys:
    # 2. Print the title and price in one line using f-string.
    # 3. Add a new key 'year' with value 2024.
    # 4. Update the price to 19.99.
    # 5. Create another dictionary named 'book2' with the same keys but different values.
    # 6. Create a list named 'library' that stores both books.
    # 7. Use a loop to print each book’s title, year, and price.



# MAIN FUNCTION
def main():
    # TODO:
    set_operations()
    # 1. Call set_operations()
    print()
    # 2. Call dictionary_practice()
    dictionary_practice()
    
    pass

# RUN PROGRAM
if __name__ == "__main__":
    main()
