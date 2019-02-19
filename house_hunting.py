total_cost = float(input("Enter the cost of your dream home? "))
portion_down_payment = total_cost * .25
current_savings = 0
month = 0
annual_salary = float(input("Enter your annual salary: "))
portion_saved = float(input("Enter the percent of you salary to save, as a decimal: "))

monthly_salary = (annual_salary / 12) 
monthly_savings = portion_saved * monthly_salary

while current_savings < portion_down_payment:
    month += 1
    interest = (current_savings * .04) / 12
    current_savings += interest
    current_savings += monthly_savings

    if current_savings >= portion_down_payment:
        print("Number of months: " + str(month)) 