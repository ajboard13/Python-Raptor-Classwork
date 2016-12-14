# Aaron Board
# 6/13/16


def score_input(tests_taken,test_score):
    stud_avg = 0.0
    index = 0
    test_score = 0.0
    while index != tests_taken:
        test_score = float(input("Enter the score for the test: "))
        while Valid_pos_float(test_score):
            test_score = float(input("Enter the score for the test: "))
        index = index + 1
        stud_avg = stud_avg +test_score
    stud_avg = stud_avg/tests_taken #Calculating the average
    return stud_avg

def student_avg(stud_avg, tests_taken):
    stud_avg = stud_avg/tests_taken #Calculating the average
    return stud_avg

def Valid_pos_int(x):
    if x < 0:
        print("Tests taken must be a positvie integer")
    try:
        return int(x) <= 0
    except ValueError:
        return False

def Valid_pos_float(x):
    if x < 0:
        print("Tests scores must be a positvie integer")
    try:
        return float(x) < 0
    except ValueError:
        return False

def main():
    name = str()
    test_score = 0.0
    class_avg = 0.0
    num_students = 0
    stop = str()
    tests_taken = int(input("Enter the number of tests taken: "))
    while Valid_pos_int(tests_taken):
        tests_taken = int(input("Enter the number of tests taken: "))
    while stop != "yes":
        index=0
        name = str(input("Enter the student's name: ")) #getting the students name
        num_students = num_students + 1
        stud_avg = score_input(tests_taken,test_score)
        class_avg = class_avg + stud_avg #adding the test avg to calss avg to calculate the class average later
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("Student's Name: %s" % name, "\nAverage : %.2f%%" % stud_avg) #outputting the results
        stop = str(input("Do you wish to stop? "))  #asking if she wishes to stop
    class_avg = class_avg / num_students
    print("\nClass Average: %.2f%%" % class_avg)
    print("goodbye") #printing goodbye

main()
