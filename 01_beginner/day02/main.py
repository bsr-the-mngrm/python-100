# DAY02 - Tip calculator - My solution

# Welcome message
print("Welcome to the tip calculator")

# Get input
total_bill = float(input("What was the total bill? $"))
tip_multiplier = 1+int(input("What percentage tip would you like to give? 10, 12 or 15? "))/100
number_of_people = int(input("How many people to split the bill? "))

# Answer
splitted_bill = "{:.2f}".format(round(total_bill*tip_multiplier/number_of_people, 2))
print(f"Each person should pay: ${splitted_bill}")