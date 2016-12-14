#Aaron Board
#6/22/16

#Declaring my variables
homes_sold = 0
home_price = [] #set home_price to my list
homes_sold_below = 0
homes_sold_above = 0
count = 0
sumprices = 0.0
avg_price = 0.0

#printing out a greeting
print("Welcome to the Botany Bay home sales calculator\n\tThis program will calculate the average selling price of the homes\n\tsold this past year. It will then determine how many homes sold\n\tabove the average and how many homes sold below the average")
print("===============================================================================\n")
homes_sold = int(input("Enter the number of homes sold: ")) # asking how many homes were sold
print("\nBotany Bay Home Sales\n*******************************")

# starting a while loop that will iterate until the number of homes sold is = to the count
while homes_sold > count:
    home_price.append(float(input("%d: $" %(count + 1)))) #adding the price for the selected home
    count = count + 1

sumprices = sum(home_price) #getting the sum of the list
avg_price = sumprices/homes_sold #dividing the sum by the number of homes sold to get the average price

#started a for loop to get the number of homes sold above and below the average
for prices in home_price:
    if prices > avg_price:
        homes_sold_above = homes_sold_above + 1
    else:
        homes_sold_below = homes_sold_below + 1

#outputtng the results
print("\nThe Average price for the homes sold was: \t$%.2f" %avg_price)
print("The number of homes sold ABOVE the average was: \t%d" %homes_sold_above)
print("The number of homes sold BELOW the average was: \t%d" %homes_sold_below)
