#lets do this



#startRating= int(input("Enter a star rating between 0 and 5: "))

#while startRating<0 or startRating>5:
    #print("Invalid Star Rating - Try Again!")
    #startRating= int(input("Enter a star rating between 0 and 5: "))

#print("Thank you!")
    


number = 7


for chance in range(3):
    guess = int(input("Guess the number: "))

    if guess == number:
        print("you guessed it right")
        break
    else:
        print("Wrong buddy")

print("\nGame over:D")       



#3nd 


for row in range(10):
    for column in range(10):
        print("%", end="")
    print()