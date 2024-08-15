# Questions for the user #

name = input("Hello User, please enter your first name: ")
q_cartprice = float(input("Hello " + name + ", please enter your total cart price: "))
q_currency = input("Now enter your currency of money: ")
q_budget = float(input("Now enter your total budget: "))
remaining_money = q_budget - q_cartprice

# Code and message if the budget is above the price #

print("------------------------------------------------")
roundingprice = round(remaining_money, 2)

if q_budget > q_cartprice:
    print("Congratulations,", name, "!")
    print("You have:", q_currency, roundingprice, "remaining left on your budget.")
    print("Calculation: ")
    print("Your Budget:", q_currency, q_budget)
    print("Your total price:", q_currency, q_cartprice)
    print(q_budget, "-", q_cartprice)
    print(q_currency, remaining_money)
    
# Code and message if the budget is equal to the price #

elif q_budget == q_cartprice:
    print("Hello", name)
    print("You have no money remaining left on your budget.")
    print("Calculation:")
    print("Your Budget:", q_currency, q_budget)
    print("Your total price:", q_currency, q_cartprice)
    print(q_currency, remaining_money)

# Code and message if the budget is below the price #

else:
    print("Hello", name)
    print("Sorry, you don't have enough money to continue this purchase.")
    print("Calculation:")
    print("Your Budget:", q_currency, q_budget)
    print("Your total price:", q_currency, q_cartprice)
    print(q_currency, remaining_money)