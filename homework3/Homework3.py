#Aaron Board
#6/27/16

#Declaring variables
OrderAmount = [0, 0, 0, 0, 0, 0]
DailyAmount = [0, 0, 0, 0, 0, 0]
items = ["Birthday Cake", "Chocolate", "French Vanilla", "Lemon", "Raspberry Cheesecake", "Red Velvet"]
item = str()
OrderSum = int()
DailySum = int()
cost = float()
OrderTotal = float()
amount = int()
DailyTotal = float()
choice = str()
cont = str()
name = str()

#Getting the name
name = str(input("Enter the name of the customer ==> "))
print("Select from the list below:\n\tB = Birthday Cake\n\tC = Chocolate\n\tF = French Vanilla\n\tL = Lemon\n\tR = Raspberry Cheesecake\n\tV = Red Velvet\n\tQ = Quit")

#Starting a while loop looking for cont == no
while cont.strip().lower() != "no":
    OrderSum = int()
    OrderTotal = float()
    OrderAmount = [0, 0, 0, 0, 0, 0]
    while cont.strip().lower() != "no":     #Started a second while loop looking for cont == no
        choice = str(input("\nEnter your selection ==> "))
        if choice.strip().upper() == "B":       #set multiple if statements looking for the selected choice
            amount = int(input("How many cupcakes do you want of this type ==> "))
            OrderAmount[0] = OrderAmount[0] + amount    #adding the amount to the correct element in the array
            DailyAmount[0] = DailyAmount[0] + amount    #adding the amount to the correct element in the array
            DailySum = DailySum + amount
            OrderSum = OrderSum + amount  #adding the total cupcakes up
            cost = amount * 2   #finding the cost
            print("Item Name:\t", items[0], "\nItem Quantity:\t", amount, "\nTotal Cost:\t$%.2f" % cost)
        if choice.strip().upper() == "C":
            amount = int(input("How many cupcakes do you want of this type ==> "))
            OrderAmount[1] = OrderAmount[1] + amount
            DailyAmount[1] = DailyAmount[1] + amount
            DailySum = DailySum + amount
            OrderSum = OrderSum + amount
            print("Item Name:\t", items[1], "\nItem Quantity:\t", amount, "\nTotal Cost:\t$%.2f" % cost)
        if choice.strip().upper() == "F":
            amount = int(input("How many cupcakes do you want of this type ==> "))
            OrderAmount[2] = OrderAmount[2] + amount
            DailyAmount[2] = DailyAmount[2] + amount
            DailySum = DailySum + amount
            OrderSum = OrderSum + amount
            print("Item Name:\t", items[2], "\nItem Quantity:\t", amount, "\nTotal Cost:\t$%.2f" % cost)
        if choice.strip().upper() == "L":
            amount = int(input("How many cupcakes do you want of this type ==> "))
            OrderAmount[3] = OrderAmount[3] + amount
            DailyAmount[3] = DailyAmount[3] + amount
            DailySum = DailySum + amount
            OrderSum = OrderSum + amount
            print("Item Name:\t", items[3], "\nItem Quantity:\t", amount, "\nTotal Cost:\t$%.2f" % cost)
        if choice.strip().upper() == "R":
            amount = int(input("How many cupcakes do you want of this type ==> "))
            OrderAmount[4] = OrderAmount[4] + amount
            DailyAmount[4] = DailyAmount[4] + amount
            DailySum = DailySum + amount
            OrderSum = OrderSum + amount
            print("Item Name:\t", items[4], "\nItem Quantity:\t", amount, "\nTotal Cost:\t$%.2f" % cost)
        if choice.strip().upper() == "V":
            amount = int(input("How many cupcakes do you want of this type ==> "))
            OrderAmount[5] = OrderAmount[5] + amount
            DailyAmount[5] = DailyAmount[5] + amount
            DailySum = DailySum + amount
            OrderSum = OrderSum + amount
            print("Item Name:\t", items[5], "\nItem Quantity:\t", amount, "\nTotal Cost:\t$%.2f" % cost)
        if choice.strip().upper() == "Q":
            quit

            ## printing the output for the first loop and asking if they wish to add more cupcakes
        print("\nCurrent Order Summary\n*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~")
        print("\tBirthday Cake\t\t%d\t\t$ " % OrderAmount[0], (OrderAmount[0]*2.00), "\n\tChocolate\t\t%d\t\t$ " % OrderAmount[1], (OrderAmount[1]*2.00), "\n\tFrench Vanilla\t\t%d\t\t$ " % OrderAmount[2], (OrderAmount[2]*2.00), "\n\tLemon\t\t\t%d\t\t$ " % OrderAmount[3], (OrderAmount[3]*2.00), "\n\tRaspberry Cheesecake\t%d\t\t$ " % OrderAmount[4], (OrderAmount[4]*2.00), "\n\tRed Velvet\t\t%d\t\t$ " % OrderAmount[5], (OrderAmount[5]*2.00))
        print("*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~")
        cont = str(input("\nWould you like to add more cupcakes to this order? "))

        ## printing the output for the second loop and asking if they wish to add more orders
    print("\nCurrent Order Summary for: ", name, "\n*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~")
    print("\tBirthday Cake\t\t%d\t\t$ " % OrderAmount[0], (OrderAmount[0]*2.00), "\n\tChocolate\t\t%d\t\t$ " % OrderAmount[1], (OrderAmount[1]*2.00), "\n\tFrench Vanilla\t\t%d\t\t$ " % OrderAmount[2], (OrderAmount[2]*2.00), "\n\tLemon\t\t\t%d\t\t$ " % OrderAmount[3], (OrderAmount[3]*2.00), "\n\tRaspberry Cheesecake\t%d\t\t$ " % OrderAmount[4], (OrderAmount[4]*2.00), "\n\tRed Velvet\t\t%d\t\t$ " % OrderAmount[5], (OrderAmount[5]*2.00))
    print("*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~")
    pretaxOrderTotal = int(OrderSum * 2)
    tax = float(pretaxOrderTotal * .06)
    OrderTotal = float(tax+pretaxOrderTotal)
    print("\tSubtotal = $", pretaxOrderTotal, "\n\tTax = $", tax, "\n\tTotal = $",OrderTotal)
    cont = str(input("\nWould you like to add another order? "))

    ## printing the totals fo the whole day
print("\nCurrent Daily Summary\n*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~")
print("\tBirthday Cake\t\t%d\t\t$ " % DailyAmount[0], (DailyAmount[0]*2.00), "\n\tChocolate\t\t%d\t\t$ " % DailyAmount[1], (DailyAmount[1]*2.00), "\n\tFrench Vanilla\t\t%d\t\t$ " % DailyAmount[2], (DailyAmount[2]*2.00), "\n\tLemon\t\t\t%d\t\t$ " % DailyAmount[3], (DailyAmount[3]*2.00), "\n\tRaspberry Cheesecake\t%d\t\t$ " % DailyAmount[4], (DailyAmount[4]*2.00), "\n\tRed Velvet\t\t%d\t\t$ " % DailyAmount[5], (DailyAmount[5]*2.00))
print("*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~")
pretaxDailyTotal = int(OrderSum * 2)
tax = float(pretaxDailyTotal * .06)
DailyTotal = float(tax+pretaxDailyTotal)
print("\tSubtotal = $", pretaxDailyTotal, "\n\tTax = $", tax, "\n\tTotal = $",DailyTotal)
