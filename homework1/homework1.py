# Aaron Board
# 6/8/16

##declaring my variables
first_name = str()
last_name = str()
full_name = str()
miles_before = int()
miles_after = int()
total_miles = int()
days = int()
daily_cost = int()
mileage_cost = float()
total_cost = float()

##gathering data
first_name = str(input("Enter first name: "))
last_name = str(input("Enter last name: "))
miles_before = float(input("Enter beginning odometer: "))
miles_after = float(input("Enter ending odometer: "))
days = int(input("Number of days rented: "))


#Calculations
full_name = first_name + " " + last_name
total_miles = miles_after - miles_before
mileage_cost = total_miles * 0.12
daily_cost = days * 15
total_cost = daily_cost + mileage_cost
mileage_cost = round(mileage_cost, 2)
total_cost = round(total_cost, 2)


#outputting results
print("     Beginning odometer reading: %d" % miles_before)
print("     Ending odometer reading: %d" % miles_after)
print("Summary of Charges for %s" % full_name)
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("Total Mileage: %d" % total_miles)
print("Mileage Cost: $", round(mileage_cost,2))
print("Rental cost: $", daily_cost)
print("===============================")
print("Total Rental Cost: $", round(total_cost,2))
