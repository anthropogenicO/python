#first excersice man

st1= "foo"
st2= "ar"
st_full= st1 +"b" + st2
print(st_full[3])



#now the class work

# password = input("Enter your password: ")

# if len(password) >= 8:
#     print("Valid password")
# else:
#     print("Password must have at least 8 characters")




# password = input("Enter your password: ")

# while len(password) < 8:
#     print("Invalid password. Must be at least 8 characters.")
#     password = input("Enter your password again: ")

# print("Valid password!")



def valid_password(password):
    flag= False
    if password.isalnum():
        flag= True

    return flag

def main():
    password = input("Enter your password :")

    while len(password)< 8:
        print ('Invalid password. Must be at least 8 characters.')
        password = input("Enter your password again: ")
    valid = valid_password(password)
    print(f"Is it valid? {valid}")


if __name__== "__main__" :
    main()
