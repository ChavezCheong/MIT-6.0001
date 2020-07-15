#Problem Set 1C: Finding the right amount to save away

#Asking for user inputs
starting_salary = float(input("Enter the starting salary: "))

#initialising state variables
semi_annual_raise = 0.07
portion_down_payment = 0.25
r = 0.04
total_cost = 1000000
months = 36
total_down_payment = portion_down_payment * total_cost

#function to calculate savings in 36 months
def calculate_savings(starting_salary, months, savings_rate, semi_annual_raise, r):
    monthly_salary = starting_salary / 12
    savings = 0
    month_count = 0
    while month_count < months:
        savings = savings + savings * r / 12 + savings_rate * monthly_salary
        month_count += 1
        if month_count % 6 == 0:
            monthly_salary += monthly_salary * semi_annual_raise
    return savings

#account for impossible tasks:
if calculate_savings(starting_salary, months, 1, semi_annual_raise, r) < total_down_payment:
    print("It is not possible to pay the down payment in three years.")
else:
    #perform bisection search
    step_count = 0
    upper_marker = 10000
    lower_marker = 0
    savings = 0
    epsilon = 100
    while abs(savings - total_down_payment) > epsilon:
        step_count += 1
        savings_count = int((upper_marker + lower_marker)/2)
        savings_rate = savings_count/10000
        savings = calculate_savings(starting_salary, months, savings_rate, semi_annual_raise, r)
        if savings > total_down_payment:
            upper_marker = savings_count
        else:
            lower_marker = savings_count

    #print results
    print(f"Best savings rate: {savings_rate}")
    print(f"Steps in bisection search: {step_count}")