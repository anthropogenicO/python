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