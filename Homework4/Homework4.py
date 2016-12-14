##Aaron Board
## 7/6/16



#setting global variables
weekdays = ["Monday ", "Tuesday", "Wednesday", "Thursday" ,"Friday ", "Saturday", "Sunday  "]
cals_consumed = [2600, 2400, 3500, 3200, 2700, 3300, 3000]
cals_burned = [150, 100, 200, 180, 250, 100, 50]


#function to find and print the totals
def Totals(weekdays,cals_consumed, cals_burned):
    total_cals = 0
    total_burned = 0
    print("*****************************************************")
    print("Day\t\tCalories Consumed\tCalories Burned")
    print("*****************************************************")
    index = 0
    while index <= 6:
        print(weekdays[index],"\t\t", cals_consumed[index], "\t\t\t", cals_burned[index])
        total_cals = total_cals + cals_consumed[index]
        total_burned = total_burned + cals_burned[index]
        index = index + 1
    print("*****************************************************")
    print("Totals  \t\t", total_cals, "\t\t\t", total_burned)

#function to find and print the differences
def Differences(weekdays, cals_consumed,cals_burned):
    index = 0
    difference = 0
    print("*****************************************************")
    print("Day\t\tCalories Left After Cycling")
    print("*****************************************************")
    while index<= 6:
        difference = cals_consumed[index] - cals_burned[index]
        print(weekdays[index], "\t\t", difference)
        index = index + 1


#function to find and print the average
def Average(cals_consumed, cals_burned):
    index = 0
    avg_burned = 0.0
    avg_cals = 0.0
    total_burned = 0
    total_cals = 0
    print("*****************************************************")
    while index<= 6:
        total_cals = total_cals + cals_consumed[index]
        total_burned = total_burned + cals_burned[index]
        index = index + 1
    avg_burned = total_burned / 7
    avg_cals = total_cals / 7
    print("Average Consumed:\t\t%.2f" %avg_cals)
    print("Average Burned: \t\t%.2f" %avg_burned)

#function to find and print the highest
def Highest(weekdays, cals_consumed, cals_burned):
    index = 0
    highest_cals = 0
    highest_burned = 0
    day_cals = ""
    day_burned = ""
    print("*****************************************************")
    while index<= 6:
        if cals_consumed[index] > highest_cals:
            highest_cals = cals_consumed[index]
            day_cals = weekdays[index]
        elif cals_burned[index] > highest_burned:
            highest_burned = cals_burned[index]
            day_burned = weekdays[index]
        index = index + 1
    print("Highest Burned:  \t",highest_burned,"\tDay:\t", day_burned)
    print("Highest Consumed:\t", highest_cals, "\tDay:\t", day_cals)

#function to find and print the lowest
def Lowest(weekdays, cals_consumed, cals_burned):
    print("*****************************************************")
    day_cals = ""
    day_burned = ""
    lowest_consumed = min(cals_consumed)
    index = cals_consumed.index(lowest_consumed)
    day_cals = weekdays[index]
    lowest_burned = min(cals_burned)
    index = cals_burned.index(lowest_burned)
    day_burned = weekdays[index]
    print("Lowest Burned:  \t",lowest_burned,"\tDay:\t", day_burned)
    print("Lowest Consumed:\t", lowest_consumed, "\tDay:\t", day_cals)

#main function
def main(weekdays, cals_consumed, cals_burned):
    #setting local variables
    cont = ""
    choice = ""
    #while loop looking for continue to equal no
    while cont.lower() != "no":
        print("*****************************************************")
        print("What do you want to do?")
        print("\n\t\tT\t=\tGet Totals\n\t\tD\t=\tFind Differences\n\t\tA\t=\tGet Average\n\t\tH\t=\tFind Highest\n\t\tL\t=\tFind Lowest\n\t\tE\t=\tExit")
        print("*****************************************************")
        choice = str(input("Enter your Choice ==> ")) #getting choice

        #if statements to determine choice and call the appropriate function
        if choice.lower() == "t":
            Totals(weekdays,cals_consumed, cals_burned)
        elif choice.lower() == "d":
            Differences(weekdays, cals_consumed,cals_burned)
        elif choice.lower() == "a":
            Average(cals_consumed, cals_burned)
        elif choice.lower() == "h":
            Highest(weekdays, cals_consumed, cals_burned)
        elif choice.lower() == "l":
            Lowest(weekdays, cals_consumed, cals_burned)
        elif choice.lower() == "e":
            print("Thanks for using the program!")
            cont = "no"
        else:
            print("No option selected, please try again.")
#calling the main function
main(weekdays, cals_consumed, cals_burned)
