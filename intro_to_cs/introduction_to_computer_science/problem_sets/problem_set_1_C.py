# You are now going to try to find the best rate of savings to achieve a 25% down payment on a $1M house in 
# 36 months.

house_total_cost = 1000000
portion_down_payment = 0.25
down_payment = house_total_cost*0.25
annual_salary = float(input("What is your annual salary? "))
semi_annual_raise = 0.07
r = 0.04

monthsAnswer = 0
high = 1.0000
low = 0.0000
Best_savings_rate = (high+low)/2 # range of 0.0000 - 1.0000, start in middle
Steps = 0
epsilon = 50
semiCounter = 1
current_savings_Answer = 0

while (abs(down_payment-current_savings_Answer) > epsilon):
    Best_savings_rate = (high+low)/2
    #print("RATE:",Best_savings_rate)

    #print("EPSILON:",down_payment,"-",current_savings_Answer,"=",abs(down_payment-current_savings_Answer))
    #print("STEP:",Steps)
    #print("MONTHS ANSWER",monthsAnswer)
    monthly_salary = annual_salary/12
    monthly_savings = monthly_salary*Best_savings_rate
    months = 0
    current_savings = 0

    while months <36:
        current_savings += (current_savings*(r/12))+monthly_savings
        months+=1
        if semiCounter == 6:
            monthly_salary*= 1+semi_annual_raise
            monthly_savings = monthly_salary*Best_savings_rate
            semiCounter = 1
            continue
        semiCounter+=1

    monthsAnswer = months
    #print("MONTHS ANSWER",monthsAnswer)
    current_savings_Answer = current_savings
    #print(down_payment,"-",current_savings_Answer,"=",abs(down_payment-current_savings_Answer))

    #print(current_savings_Answer,"A")
    #print(down_payment,"B")
    #print("SAVINGS:",current_savings_Answer)

    if current_savings_Answer > down_payment:
        high = Best_savings_rate
        #print("HIGH",high)
    else:
        low = Best_savings_rate
        #print("LOW",low)

    Steps+=1
    if Steps > 100:
        print("It is not possible to pay the down payment in 3 years.")
        break

if Steps <100:
    print("Best Savings Rate:",Best_savings_rate)
    print("Savings:",current_savings_Answer)
    print("Months:",months)
    print("Steps in bisection search:",Steps)
