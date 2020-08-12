interest_bond = input("Enter if you want to calculate interest or bond: ") #Ask user what they want to calculate
if interest_bond.lower() == "interest": #If interest is chosen run, the if statement below
    money_dep = int(input("How much money are you planning on depositing? ")) 
    persentage = float(input("What is the interest rate on your deposit? (only the number is needed): "))
    dperc = persentage / 100 #Converting a percentage into a decimal
    num_years = int(input("How many years would you like to invest for? ")) 
    comp_simple = input("Would you like simple or compound interest? ") #Ask user is they want to use simple or compound interesr
    if comp_simple.lower() == "simple":
        print(money_dep * (1 + dperc * num_years)) #Print out answer for simple interest
    elif comp_simple.lower() == "compound":
        print(money_dep * (1 + dperc) ** num_years) #Print out answer for compound interest
if interest_bond.lower() == "bond": #If bond is chosen, run the if statement below
    pres_value = int(input("Enter the present value of your house: "))
    interest_rate = float(input("Enter interest rate on bond: "))
    bperc = interest_rate / 100 #Converting a percentage into a decimal
    num_months = int(input("Enter how many months to pay of bond: "))
    over_all_amount = ((interest_rate * pres_value) / 1-(1 + interest_rate) ** -num_months) 
    print(over_all_amount / 120) #Print out answer for amount on bond