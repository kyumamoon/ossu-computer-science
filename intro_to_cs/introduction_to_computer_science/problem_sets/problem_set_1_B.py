# Part B: Saving, with a raise
# Background 
# In Part A, we unrealistically assumed that your salary didn’t change.  But you are an MIT graduate, and
# clearly you are going to be worth more to your company over time! So we are going to build on your
# solution to Part A by factoring in a raise every six months. 
# In ps1b.py​, copy your solution to Part A (as we are going to reuse much of that machinery).  Modify
# your program to include the following
#   1. Have the user input a semi-annual salary raise semi_annual_raise​ (as a decimal percentage)
#   2. After the 6th month, increase your salary by that percentage.  Do the same after the 12th
#   the 18th  month, and so on. 

# Write a program to calculate how many months it will take you save up enough money for a down
# payment.  LIke before, assume that your investments earn a return of r​ = 0.04 (or 4%) and the
# required down payment percentage is 0.25 (or 25%).  Have the user enter the following variables:
#   1. The starting annual salary (annual_salary)
#   2. The percentage of salary to be saved (portion_saved)
#   3. The cost of your dream home (total_cost)
#   4. The semi­annual salary raise (semi_annual_raise

portion_down_payment = 0.25
current_savings = 0
r = 0.04
annual_salary = float(input("WHAT IS ANNUAL SALARY: "))
monthly_salary = annual_salary/12
portion_saved = float(input("PERCENTAGE OF SALARY WANT TO PUT ASIDE TO SAVE (In decimal): "))
monthly_savings = monthly_salary*portion_saved
total_cost = float(input("COST OF DREAM HOME: "))
down_payment = total_cost*portion_down_payment
semi_annual_raise = float(input("WHAT IS SEMI-ANNUAL RAISE PERCENTAGE TO SALARY (In decimal):"))
print("DOWN PAYMENT:",down_payment)

months = 0
semiCounter = 1
while current_savings <= down_payment:
    current_savings += (current_savings*(r/12))+monthly_savings
    months+=1
    #print("MONTH:",months,"CURRENT SAVINGS:",current_savings)
    if semiCounter == 6:
        monthly_salary*= 1+semi_annual_raise
        monthly_savings = monthly_salary*portion_saved
        semiCounter = 1
        continue
    semiCounter+=1
    
print(current_savings)
print(months)
