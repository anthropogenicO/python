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





