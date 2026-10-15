#here we will do the first excersise

def addNum(num1, num2):
    answer= num1+num2
    print("Answer:", answer)


def substractNum(num1, num2):
    answer= num1-num2
    print("answer:", answer)


#here is the main fuction

def main():
    num1= int(input("Enter first numbner: "))
    num2= int(input("Enter second number: "))

    menuoption= input("Enter add or substract: ")
    
    if menuoption== "add":
        addNum(num1, num2)
    else:
        substractNum(num1, num2)

main()

