#Aaron Board
# 7/6/16


## Declaring variables
fahr = 0.0
cel = 0.0
feet = 0.0
meters = 0.0

## function to convert from fahrenheit to celsius
def fahr_to_cel(fahr):
    cel = (fahr - 32) *(5/9)
    print(fahr , "degrees = ",cel,"degrees celsius")


## function to convert from feet to meters
def feet_to_meters(feet):
    meters = feet * 0.305
    print(feet, "feet = ", meters, "meters")



## main function
def main():
    #declaring local variables
    cont = ""
    choice = ""
    print("Welcome to the Metric Conversion Program\nThis program will take a unit of measurement and convert\n\tit to degrees celsius or meters")
    print("***********************************************************************")

    #while loop looking for continue to equal "no"
    while cont.lower() != "no":
        print("\nHere are your choices:\n\tC for Celsius\n\tM for Meters\n\tE for Exit")
        choice = str(input("\nEnter your selection: "))    #getting choice
        #determining choice
        if choice.lower() == "c":   
            fahr = float(input("Enter degrees Fahrenheit: "))
            fahr_to_cel(fahr) #calling funtion
        elif choice.lower() == "m":
            feet = float(input("Enter feet: "))
            feet_to_meters(feet)  #calling funtion
        elif choice.lower() == "e":  #exits program by setting cont = "no"
            print("Thank you for using our program")
            cont = "no"
        else:
            print("Sorry you did not enter a C, M, or E\nPlease try again.") #error
        

main()
