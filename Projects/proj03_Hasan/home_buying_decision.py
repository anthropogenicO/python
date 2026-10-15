#program: home_buying_decision.py
#name : Md Mridul Hasan
#lab sec : CS-1110-545 
#check if the house is affordable using the project's budget rule


#this function checks both amounts and returns the home buying decision
def make_home_buying_decision(home_price, budget, mortgage_payment):


    #both the house price and the monthly payment must be within the budget
    if home_price <= budget and mortgage_payment <= budget:
        decision = "Affordable"
    else:
        decision = "Not affordable"




    return decision
