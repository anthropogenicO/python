#program: budget_calculation.py
#name : Md Mridul Hasan
#lab sec : CS-1110-545
#calculate the maximum home price based on income, savings and monthly expensess


#this function takes the financial information and returns the home budget
def calculate_budget(annual_income, savings, monthly_expenses):

    #use 3 years of income, add savings, then subtract 2years of expenses
    max_home_price = annual_income * 3 + savings - (monthly_expenses * 12 * 2)



    return max_home_price
