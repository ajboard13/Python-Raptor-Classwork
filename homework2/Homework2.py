##Aaron Board
## 6/15/16

#declaring variables
date_ordered = str()
date_needed = str()
name = str()
size = str()
num_shirts = int()
shirt_price = float()
total_price = float()
current_total = float()
add_more = str()

#printing a welcome
print("Welcome to Custom T's")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

#getting a name and dates
name = str(input("Enter the name of the customer: "))
date_ordered = str(input("Enter the date the order is taken: "))
date_needed = str(input("Enter the date the order is needed: "))

#Starting a while loop with the condition of add_more not being equal to "no"
while add_more != "no":
    choice = str()
    size = str(input("Select from the following size categories: \n\tC = Children\n\tA = Adult\n\tB = Big Sizes\n\nEnter your selection:\t")) #Getting an input for size
    num_shirts = int(input("\nHow many shirts do you need in this size? ")) #getting an input for the number of shirts

    #Determining what size was selected and setting the appropriate price
    if size == "A":
        shirt_price = 6.00
    elif size == "B":
        shirt_price = 7.00
    elif size == "C":
        shirt_price = 4.00
    else:
        print("Wrong size category entered")
        break
    print("\nNow we will determine if you would like any extras")

#determining if the customer wants extras and setting the shirt price appropriately
    choice = str(input("\nWould you like to add any extra artwork? "))
    if choice == "yes":
        shirt_price = shirt_price + 2.00
    choice = str(input("Would you like to add any monogramming? "))
    if choice == "yes":
        shirt_price = shirt_price + 1.5
    choice = str(input("Would you like to use premium fabric? "))
    if choice == "yes":
        shirt_price = shirt_price + 2.25
    choice = str(input("Would you like the shirts to be long sleeved? "))
    if choice == "yes":
        shirt_price = shirt_price + 3.0
    #finding the current total and grand total
    current_total = float(shirt_price * num_shirts)
    total_price = total_price + current_total #accumulator

    #poutputting results and asking if the customer would like to add more shirts
    print("\nThe cost per shirt with the included extras will be: $%.2f" % shirt_price)
    print("The total for the number of shirts with these extras will be: $%.2f" % current_total)
    add_more = str(input("\nWould you like to add more shirts to the order? "))

    #outputting final results
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("Custom T's Order Form")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("Customer: %s" % name)
print("Order Date: %s" % date_ordered)
print("Date Needed: %s" % date_needed)
print("\nThe total price will be $%.2f" % total_price)
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("\nThank you for your order!")
