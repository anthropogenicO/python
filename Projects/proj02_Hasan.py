#program: proj02_hasan.py
#name : Md Mridul Hasan
#Lab section : CS-1110-545 (Time 10:30 AM - 12:20 PM)
#lets create a salary calculator porgram that shows the total pay for any employee based on their level, base salary, performace each month(items sold).


#constants
FIRST_PAY_PER_ITEM_P =75
SECOND_PAY_PER_ITEM_P =125

FIRST_PAY_PER_ITEM_M = 60
SECOND_PAY_PER_ITEM_M = 100

FIRST_PAY_PER_ITEM_B = 50
SECOND_PAY_PER_ITEM_B = 75

#state 0
#now fix nd do the state 1
#state 2
#done state 3 everythign works perfectly yay:D


another_employee= "Y"
while another_employee == "Y":

    name = input("Enter Employee’s Name: ")
    base_salary = float(input("Enter Monthly Base: "))

    #lets work on tier validation
    tier = input("Enter Tier (B, M, or P): ")
    tier = tier[0]
    tier = tier.upper()
    #put the loop in
    while tier !="P" and tier !="M" and tier !="B": #if not P M B then error
        print ("Tier", tier, "is not a legitimate tier value.")
        tier = input("Enter Tier (B, M, or P): ")
        tier = tier[0]
        tier = tier.upper()

    #now lemme do this one validation
    item_sold = int(input("Enter Items Sold: "))
    while item_sold <= 0: #less thanmeans not positive num
        print("Invalid number for Items Sold.")
        item_sold = int(input("Enter Items Sold: "))


#now the main part :calculation
    if tier == "P":
    
        if item_sold > 19 and item_sold <= 25:
            commissioned_item = item_sold - 19
            # commission for selling more than 19
            commission =  commissioned_item * FIRST_PAY_PER_ITEM_P
    

        elif item_sold > 25:
            first_batch = 25 #here till 25 item we are in forst batch
            commission_item_first_batch = first_batch -19
            #commission for selling more than 19
            #we did this logic cuz we need the numbers of items that pay us 75 dollar commision per item.
            commission_first_batch =  commission_item_first_batch * FIRST_PAY_PER_ITEM_P

            #now we have to calculate the commission for sold items more than 25
            commission_item_second_batch = item_sold -25 #we did this logic cuz we need the numbers of items that pay us 125 dollar commision per item.
            #commission for more than 25
            commission_second_batch =  commission_item_second_batch * SECOND_PAY_PER_ITEM_P
        
            #actual commission
            commission = commission_first_batch + commission_second_batch


        else:
            commission = item_sold * 0 #less than 19 so then there is no commission
        

    #now lets calcualte the actula salary for tier P
        salary = base_salary + commission


    #lets do the exact same thing for tier M
    elif tier == "M":
        if item_sold > 14 and item_sold <= 20:
            commissioned_item = item_sold - 14
            # commissioon for this one
            commission =  commissioned_item * FIRST_PAY_PER_ITEM_M
    

        elif item_sold > 20:
            first_batch = 20 #here till 20 item we are in forst batch
            commission_item_first_batch = first_batch -14
            #same logic as the tier P
            # commission
            commission_first_batch =  commission_item_first_batch * FIRST_PAY_PER_ITEM_M

            #now we have to calculate the commission for sold items more than 20
            commission_item_second_batch = item_sold -20 #same
            # commission for thisone
            commission_second_batch =  commission_item_second_batch * SECOND_PAY_PER_ITEM_M
        
            #actual commission
            commission = commission_first_batch + commission_second_batch


        else:
            commission = item_sold * 0 #less than 14 so then there is no commission
        
    #now lets calcualte the actual salary for tier M
        salary = base_salary + commission



    #tier B
    elif tier == "B":
        if item_sold > 9 and item_sold <= 15:
            commissioned_item = item_sold - 9
            # commission for this one
            commission =  commissioned_item * FIRST_PAY_PER_ITEM_B
        

        elif item_sold > 15:
            first_batch = 15 #here till 15 item we are in forst batch
            commission_item_first_batch = first_batch -9
            #SAME LOGIC
            # commission
            commission_first_batch =  commission_item_first_batch * FIRST_PAY_PER_ITEM_B

            #now we have to calculate the commission for sold items more than 15
            commission_item_second_batch = item_sold -15 #same logic
            # commission for thisone
            commission_second_batch =  commission_item_second_batch * SECOND_PAY_PER_ITEM_B
            
            #actual commission
            commission = commission_first_batch + commission_second_batch


        else:
            commission = item_sold * 0
        

    #actula salary for tier B
        salary = base_salary + commission


    #main output
    print(f"{name}, Tier: {tier}, Sold {item_sold} items, Monthly Payment: {salary:.2f}")

    #warning thingy
    if tier == "P" and item_sold <20:
        print ("WARNING: Sales must improve to stay in Tier P") #msg
    if tier == "M" and item_sold <15:
        print ("WARNING: Sales must improve to stay in Tier M") 
    if tier == "B" and item_sold <10:
        print ("WARNING: Sales must improve.")
    

    #just change the another_employee value
    another_employee= input("Do you want to enter another employee? ")
    another_employee = another_employee[0]
    another_employee = another_employee.upper()

#complete