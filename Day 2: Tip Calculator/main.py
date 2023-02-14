# Welcome
print("Welcome to the tip calcuator.")

# Get the input from the user
bill = float(input("What was the total bill?\n"))
tip = int(input("What percentage tip would you like to give? 10%, 12% or 15%\n"))
people = int(input("How many people to split the bill?\n"))

# Calculate the total per person shoud pay
tip_percent = (tip / 100) + 1
bill_tip = ((bill * tip_percent) / people)
per_person = "{:.2f}".format(bill_tip)

# Print answer
print(f"Each person should pay: £{per_person}")
