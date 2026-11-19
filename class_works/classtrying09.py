import random


def generate_numbers():
    num1 = random.randint(1, 9)
    num2 = random.randint(1, 9)

    return num1, num2

def main():
    ask_again = 'y'

    while ask_again == 'y':
    
        num1, num2 = generate_numbers()

        answer = int(input(f"How much is {num1} times {num2}? "))

        while answer != num1 * num2:
            print("Incorrect answer. Please try again.")
            answer = int(input(f"How much is {num1} times {num2}? "))

        print("Very good!") 
        ask_again = input("Do you wish to continue? ")
    
main()