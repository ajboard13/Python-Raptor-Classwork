# Aaron Board
# 6/13/16

#declring my variables
minutes = 5
ellip_cals_min = 6
bike_cals_min = 11
walk_cals_min = 4
cals_burned_ellip = int()
cals_burned_bike = int()
cals_burned_walk = int()

#printing the column headers
print("Minutes\tElliptical\tBiking\tWalking")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

#starting my count loop
while minutes <= 30: #checking to see if minutes is greater than 30
    cals_burned_ellip = ellip_cals_min * minutes #calculating calories burned
    cals_burned_bike = bike_cals_min * minutes #calculating calories burned
    cals_burned_walk = walk_cals_min * minutes #calculating calories burned
    print(minutes,"\t", cals_burned_ellip,"\t","\t", cals_burned_bike,"\t", cals_burned_walk) #printing the results
    minutes = minutes + 5 #adding 5 to the minutes
