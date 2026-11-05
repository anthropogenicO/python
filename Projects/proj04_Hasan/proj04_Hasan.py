#Program : proj04_Hasan.py
#Project 4
#Author: Md Mridul Hasan
#Lab section : CS-1110-545
#Description: Read the old customer file and then process bank transactions,
#and write the updated accounts to a new customer file.


def get_number(one_line):
    #first 6 char are the account number
    account_number = int(one_line[0:6])
    return account_number


def get_balance(one_line):
    #skip the acc number and the space, then take 10 char
    account_balance = float(one_line[7:17])
    return account_balance


def get_name(one_line):
    #the name starts at index 18, remove only the ending 
    account_name = one_line[18:].rstrip("\r\n")
    return account_name


def get_amount(prompt):
    #lets keep asking until the amount is numeric and greater than 0
    valid_amount = False

    while not valid_amount:
        try:
            amount = float(input(prompt))

            if amount <= 0:
                print("INVALID INPUT: Please enter a numeric value greater than 0.")

            elif not amount < float("inf"):
                #nan and infinity are not usable amounts of money
                print("INVALID INPUT: Please enter a numeric value.")

            else:
                valid_amount = True

        except ValueError:
            #words and blank input can't be converted into a float
            print("INVALID INPUT: Please enter a numeric value.")

    return amount


def process_customer(one_line, new_file, min_balance, max_balance):
    #now lets get the three parts using the required function
    account_number = get_number(one_line)
    balance = get_balance(one_line)
    name = get_name(one_line)

    account_closed = False
    command = ""

    print(f"Verifying input: {account_number} {balance:.2f} {name}")

    #keep working on this customer until we advance or close the account
    while command != "a" and not account_closed:
        command = input("Enter a command (a,c,d,w): ")

        if command == "d":
            amount = get_amount("Enter deposit amount: ")
            new_balance = balance + amount

            if new_balance > max_balance:
                print("Deposit not processed because the balance would exceed 9999999.99.")
            else:
                #round to 2 decimals cause the balance is money
                balance = round(new_balance, 2)

        elif command == "w":
            amount = get_amount("Enter withdrawal amount: ")
            new_balance = balance - amount

            if new_balance < min_balance:
                print("Withdrawal not processed because there is not enough money.")
            else:
                #this also prevents tiny float errors when reaching 0.00
                balance = round(new_balance, 2)

        elif command == "c":
            if balance == min_balance:
                print("Account is closed")
                account_closed = True
                #lets advance immediately after closing
            else:
                print("Account not closed because money is still in it.")

        elif command != "a":
            #check the whole command, so blank input and extra letters are invalid
            print(f"Entered an invalid command {command}.")

    print(f"New balance: {account_number} {balance:.2f} {name}")

    #closed acc shouldn't be written to the new file
    if not account_closed:
        if balance == get_balance(one_line):
            #if nothing changed, keep the og line exactly the same
            new_file.write(one_line)
        else:
            #keep the account, spaces name and line ending from the old record
            #but replace the 10-chara balance field
            new_line = one_line[:7] + f"{balance:10.2f}" + one_line[17:]
            new_file.write(new_line)


def main():
    #constants are inside main and I didn't use any global variable
    SENTINEL_CODE = 999999
    MIN_BALANCE = 0.00
    MAX_BALANCE = 9999999.99

    #first lets make both file names from the prefix
    try:
        file_prefix = input("Enter a file prefix: ")
    except EOFError:
        print("\nInput ended before a file prefix was entered.")
        return

    old_file_name = file_prefix + "_old.txt"
    new_file_name = file_prefix + "_new.txt"

    try:
        #newline="" keeps the original line endings when reading and writing
        old_file = open(old_file_name, "r", newline="")
    except FileNotFoundError:
        print(f"The file name {old_file_name} does not exist")
        return
    except OSError:
        print(f"The file name {old_file_name} could not be opened for reading")
        return
    except ValueError:
        print("The file prefix is invalid")
        return

    try:
        new_file = open(new_file_name, "w", newline="")
    except OSError:
        print(f"The file name {new_file_name} could not be opened for writing")
        old_file.close()
        return
    except ValueError:
        print("The file prefix is invalid")
        old_file.close()
        return

    try:
        one_line = old_file.readline()

        #now lets process one customer at a time until the sentinel
        while get_number(one_line) != SENTINEL_CODE:
            process_customer(one_line, new_file, MIN_BALANCE, MAX_BALANCE)
            one_line = old_file.readline()

        #copy the sentinel too...
        new_file.write(one_line)

    except EOFError:
        print("\nInput ended before processing finished. The new file is incomplete.")
    except KeyboardInterrupt:
        print("\nProcessing stopped. The new file is incomplete.")
    except OSError:
        print("An error occurred while reading or writing the customer files.")
    finally:
        #close both filessss
        old_file.close()
        new_file.close()


if __name__ == "__main__":
    main()

#done
