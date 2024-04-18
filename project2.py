total_bill = (float(input('Welcome to the tip calculator. \n What was the total bill? $')))
num_of_people = int(input('How many people to split the bill? '))
tip_percentage = float(input('What percentage tip would you like to give? '))
final_amount = round(total_bill*(1+ 0.01 * tip_percentage)/num_of_people,2)
final_amount = "{:.2f}".format(final_amount)
print(f"Each person should pay: ${final_amount}")

