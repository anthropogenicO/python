#name: Md Mridul Hasan
#Write a gretting messeage
#this was the first problem

print ("Hello, Python Learner!")
print ("Welcome to CS/CYCS 1110 Lab")


#store and display user's name properly
#2nd problem

first_name = input("Enter Your First Name: ")
last_name = input("Enter your Last Name: ")

full_name = first_name + " " + last_name

print ("Hello,", full_name + "!")


#ask to put two integers and then calculates the product
#3rd problem

first_integer = int(input("Enter First Integer: "))
second_integer = int(input("Enter Second Integer: "))

product = first_integer * second_integer

print("The product of the two integers is", product)


#calculates the area of a circle
#4th problem

rad = float(input("Enter the radius of the circle: "))
phi = float(input("Enter the value of pi: "))

area = phi * rad * rad

print("The area of the circle is", area)


#total cost of a item after tax
#5th problem

itemcost = float(input("Enter the price of the item: "))

tax = itemcost * 5 / 100

aftertaxcost = itemcost + tax

print("The toal cost of the item after tax is", aftertaxcost)
                 