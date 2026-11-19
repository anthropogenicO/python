#shit today we will learn a lot of stuff


#while condition

#keep_going = "h"

#while keep_going == "h":
    #print("Hello, man")

    #keep_going = input("Do you want to continue? (h for yes): ")



#for i in range(10, 81, 10):
    #print(i, end=", ")


number = 7


for chance in range(3):
    guess = int(input("Guess the number: "))

    if guess == number:
        print("you guessed it right")
        break
    else:
        print("Wrong buddy")

print("\nGame over:D")       






#here is the accumulator
total = 0
keep_going = "y"

while keep_going == "y":
    num = int(input("enter a number: "))
    total = total + num
    keep_going = input("is there another nymber to read? ")
print(f"The total of the numbers is {total}")



#exceside number 1

x = 1
y = 0

for i in range(5):
    x = x * 2
    y = y + 10

print("x =", x)
print("y =", y)
    