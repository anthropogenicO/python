print(1, end="")
print(4, end="")
print(5 )


num= 123456789123456789.384940
print(f"{num:,.2f}")


tem= int(input("Enter the tempurature today: "))

if tem <30:
    print("A little cold, isn't it")

else: print("it's normal weather out here")



password= input("Enter the password: ")

Confirm_pass= input("Confirm the password: ")

if password == Confirm_pass:
    print("Password matched")
    
else:
    print("Password didn't match, think harder man")



    points_value= int(input("Enter the points value: "))

if points_value >= 10 and points_value <= 100:
    print("Valid points")
    
else:
    print("Invalid points, sorry")



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
                 








#frist problem
student_score= int(input("Enter the score of the student: "))

#lets do the main work
if student_score >= 90:
    print(" Grade A")
elif student_score >= 80:
        print("Grade B")
elif student_score >= 70:
    print("Grade ")
elif student_score >= 60:
    print("Grade D")

else: 
    print("Grade F")




#second problem

input_number= int(input("Enter a number: "))

#lets put the odd and even logic
if input_number % 2 == 0:
    print(input_number, "is an even number")

else:

   print(input_number, "is an odd number")


#third problem

first_number= float(input("Enter the first decimal number: "))
second_number= float(input("Enter the second decimal number: "))
third_number= float(input("Enter the third decimal number: "))

#now lets do the work"D

if first_number > second_number and first_number > third_number:
    print(f"The largest number is {first_number:.1f}")
elif second_number > first_number and second_number > third_number:
    print(f"The largest number is {second_number:.1f}")

else:
    print (f"The largest number is {third_number:.1f}")











#Program : proj01_hasan.py
#Name :  Md Mridul Hasan
#Convert the distance in chains to several other units of distance, and then calculate the walking time needed to cover this distance by assuming a average walking speed of 3.1 miles per hour.


def main():

    distance_in_chains= float(input("Welcome to the NYC Subway distance converter!"
         "\n" #used "\n " for a blank line, and to break the lines
         "\n" 
         "Enter the distance in Chains: "))

     #store the conversion constant of units
    feet_per_chain= 66 
    meters_per_foot= 0.3048
    feet_per_mile= 5280
    meters_per_kilometer= 1000
       #should be unchanged

     #convert input into other units  
    distance_in_feet= distance_in_chains* feet_per_chain
    distance_in_meter= distance_in_feet * meters_per_foot
    distance_in_miles= distance_in_feet/feet_per_mile       #1mile = 5280 feet
    distance_in_kilometers= distance_in_meter/meters_per_kilometer   

     #calculate the walking distance
    speed_mph= 3.1   #average walking speed in 3.1 miles/hour

    time_hours= distance_in_miles / speed_mph

    #hours to mins, by multiplying 60
    walking_time_in_mins= time_hours * 60

    #now lets print
    print(
         "\n"
         "Distance:", f"{distance_in_chains:.3f}", "chains", "\n"  #used f-string to show only 3 decimals
         "Meters:", f"{distance_in_meter:.3f}" "\n"
         "Feet:", f"{distance_in_feet:.3f}" "\n"
         "Miles:", f"{distance_in_miles:.3f}" "\n"
         "Kilometers:", f"{distance_in_kilometers:.3f}" 
         "\n"
         "\n"
         "Walking time:", f"{walking_time_in_mins:.1f}", "minutes"  #.1f to show only 1 decimal
         "\n" #used "\n " for a blank line, and to break the lines
         "\n"
         "Thank you for using the converter. Goodbye:D")



if __name__ == "__main__":
    main()

#used the def main()






if item_sold <= 19:
        commission = item_sold * 0 #less than 19 so then there is no commission