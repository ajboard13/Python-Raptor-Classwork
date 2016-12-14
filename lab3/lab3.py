#Aaron Board
# 6/13/16

# Declaring my variables
destination = str()
miles = int()
MPG = int()
gallon_cost = float()
gallons_used = float()
trip_cost = float()
cont = str("Yes")

#starting my while loop
while cont != "No" and cont == "Yes": #determining if they wish to continue
    destination = str(input("Where are you going? "))  #gathering inputs
    miles = float(input("How many miles will you drive? "))  #gathering inputs
    MPG = int(input("Enter the MPG for your car: "))  #gathering inputs
    gallon_cost = float(input("What is the current price for a gallon of gas? "))  #gathering inputs
    gallons_used = miles / MPG  #calculating MPG
    trip_cost = gallons_used * gallon_cost  # calculating the trip cost
    print("Your trip to:     %s" % destination)  #outputting results
    print("     Total Miles: %d" % miles)  #outputting results
    print("     MPG:     %d" % MPG)  #outputting results
    print("     Gas Consumption: %.2f" % gallons_used)  #outputting results
    print("-----------------------------------")
    print("     Trip cost: $%.2f" % trip_cost)  #outputting results
    print(" ")
    cont = str(input("Do you wish to continue? (Yes or No) "))  #asking if they wish to continue
print("Goodbye")  #outputting goodbye
