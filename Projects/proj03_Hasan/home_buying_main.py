#prg: home_buying_main.py
#namee : Md Mridul Hasan
#Lab Section : CS-1110-545
#get the buyer's information and use the three modules to check each house.


#import the three files to use the functions
import budget_calculation
import mortgage_calculation
import home_buying_decision



#main handles the inputs, calls the functions nd repeats for another house
def main():

    another_house = "Y"
    while another_house == "Y":

        #first let's get the financial information for the budget
        annual_income = float(input("Enter your annual income: "))
        savings = float(input("Enter your savings: "))
        monthly_expenses = float(input("Enter your monthly expenses: "))

        #send the values to the budget function and then keep the returned budgett
        budget = budget_calculation.calculate_budget(
            annual_income, savings, monthly_expenses
        )

        #now get the house price and down payment
        home_price = float(input("Enter the price of the house you want to buy: "))
        down_payment = float(input("Enter your down payment: "))

        #keep asking if the down payment is equal to or more than the house price
        while down_payment >= home_price:
            print("Invalid input: Down payment cannot exceed or equal the home price.")
            down_payment = float(input("Enter your down payment: "))

        interest_rate = float(input("Enter the annual interest rate for the mortgage (%): "))
        loan_term = int(input("Enter the loan term in years: "))

        #send the loan information to the mortgage function
        mortgage_payment = mortgage_calculation.calculate_mortgage(
            home_price, down_payment, interest_rate, loan_term
        )

        #use the budget nd monthly payment to get the decision
        decision = home_buying_decision.make_home_buying_decision(
            home_price, budget, mortgage_payment
        )


        #mainoutput
        print("Decision:", decision)
        print()



        #just change the another_house value to control the loop
        another_house = input("Do you want to buy another house? ")

        #take the first character and capitalize it
        if another_house != "":
            another_house = another_house[0]
            another_house = another_house.upper()

        #blank line before the next house
        print()



if __name__ == "__main__":
    main()
