# Aaron Board
# 6/13/16


#Declaring my variables
name = str()
test_score = 0.0
class_avg = 0.0
num_students = 0
stop = str()

#starting the while loop to look for a "yes"
while stop != "yes":
    test_avg = 0.0 #declaring variables in the loop so they reset
    tests_taken = 0  #declaring variables in the loop so they reset
    name = str(input("Enter the student's name: ")) #getting the students name
    num_students = num_students + 1
        #starting a while loop to look for tests taken
    while tests_taken <=2:  
        test_score = float(input("Enter the score for this test: ")) #asking fo the test score
        tests_taken = tests_taken+1 #adding 1 to tests taken
        test_avg = test_avg + test_score #adding the test score to test average to calculate the average later
    test_avg = (test_avg/3)  #Calculating the average
    class_avg = class_avg + test_avg #adding the test avg to calss avg to calculate the class average later
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("Student's Name: %s" % name, "\nAverage : %.2f%%" % test_avg) #outputting the results
    stop = str(input("Do you wish to stop? "))  #asking if she wishes to stop
class_avg = class_avg / num_students
print("\nClass Average: %.2f%%" % class_avg)
print("goodbye") #printing goodbye
