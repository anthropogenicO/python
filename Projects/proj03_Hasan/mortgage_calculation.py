#prg: mortgage_calculation.py
#name : Md Mridul Hasan
#lab section : CS-1110-545
#calculate the monthly mortgage pay for the house.


#this function takes the loan information and returns the monthly payment
def calculate_mortgage(home_price, down_payment, interest_rate, loan_term):


    #change the yearly percentage to a decimal then divide by 12 for each month
    monthly_interest_rate = interest_rate / 100 / 12

    #years to months, so this is the total number of payments
    num_payments = loan_term * 12
    #subtract the down payment to get the amount we need to borrow
    loan_amount = home_price - down_payment

    #now lets calculate the monthly payment using the mortgage formula
    monthly_payment = loan_amount * (
        monthly_interest_rate * (1 + monthly_interest_rate) ** num_payments
    ) / ((1 + monthly_interest_rate) ** num_payments - 1)
    return monthly_payment
