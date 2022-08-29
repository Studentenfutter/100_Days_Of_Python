# Tip calculator
#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
bill = input("What was the total bill? $")
tip = input("What percentage tip would you like to give? 10, 12, or 15?")
people = input("How many people to split the bill?")

bill = float(bill)
tip = float(tip)
people = int(people)

calculated_tip= (bill / people) * (tip / 100)
rounded_tip = calculated_tip

split_bill = round((bill / people) + rounded_tip, 2)
print(f"Each person should pay: ${split_bill}")
