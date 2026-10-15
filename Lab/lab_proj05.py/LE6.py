def get_id(one_line):
    # TODO: Return the first 6 characters as a stripped string.
    return one_line[:6].strip()


def get_quantity(one_line):
    # TODO: Extract the quantity and return it as an integer.
    return int(one_line[7:11].strip())


def get_name(one_line):
    # TODO: Return the name from index 12 onward, stripped.
    return one_line[12:].strip()


def print_item(item_id, qty, name):
    # TODO: Print in this format: A10203 (Hammer) - 50
    print(f"{item_id} ({name}) - {qty}")



def main():
    SENTINEL_CODE = "END"

    # TODO: Open Items_old.txt for reading.
    oldfile = open("item_old.txt", "r")
    # TODO: Open Items_new.txt for writing.
    newfile = open("items_new.txt", "w")

    # TODO: Read the first line and remove the newline.
    line = oldfile.readline().strip()

    # TODO: Loop until the line equals SENTINEL_CODE.
    while line != SENTINEL_CODE:

        # TODO: Use the helper functions to extract the fields.
        item_id = get_id(line)
        qty = get_quantity(line)
        name = get_name(line)

        # TODO: Display the item using print_item().
        print_item(item_id, qty, name)


        # TODO: Ask for a new quantity and convert it to an integer.
        new_qty = int(input("Enter new quantity: "))

        # TODO: While the quantity is negative:
            # Display an error message.
            # Ask for a new quantity again.
        while new_qty < 0:
            print("Quantity must be a positive integer")
            new_qty = int(input("Enter new quantity: "))

        # TODO: Write the updated record to the new file.
        # Use an ID field of width 6 and a right-aligned quantity
        # field of width 4, separated by spaces, followed by the name.
        newfile.write(f"{item_id:6} {new_qty:>4} {name}\n")


        # TODO: Read the next line.
        line = oldfile.readline().strip()

    # TODO: Write END to the new file.
    newfile.write("END\n")

    # TODO: Close both files.
    oldfile.close()
    newfile.close()



if __name__ == "__main__":
    main()