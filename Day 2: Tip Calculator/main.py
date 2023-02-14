# Welcome
print("Welcome to the tip calcuator.")

# Get the input from the user
bill = input("What was the total bill?\n")
tip = input("What percentage tip would you like to give? 10%, 12% or 15%\n")
people = input("How many people to split the bill?\n")

# Calculate the total per person shoud pay
tip_percent = (int(tip) / 100) + 1
bill_tip = ((float(bill) * float(tip_percent)) / int(people))
per_person = round(bill_tip, 2)

# Print answer
print(f"Each person should pay: £{per_person}")
