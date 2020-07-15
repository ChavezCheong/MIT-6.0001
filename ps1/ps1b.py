#Problem Set 1B: Saving, with a raise

#Asking for user inputs
annual_salary = float(input("Enter your annual salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost = float(input("Enter the cost of your dream home: "))
semi_annual_raise = float(input("Enter the semi-annual_raise, as a decimal: "))

#Initialising state variables
portion_down_payment = 0.25
current_savings = 0
r = 0.04
monthly_salary = annual_salary / 12.0

#Counting months
month_count = 0
while current_savings < portion_down_payment *  total_cost:
    current_savings = current_savings + current_savings * r / 12 + portion_saved * monthly_salary
    month_count += 1
    if month_count % 6 == 0:
        monthly_salary += monthly_salary * semi_annual_raise
print("Number of months: " + str(month_count))
