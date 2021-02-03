"""Problem Statement:
        Student wants to know his grade based on his GPA.
    
    This program is accepting real time input and performing validations for the value provided."""

#UDF(user defined function) definition
def know_my_grade():
    #Initialize variables
    my_gpa='NA'
    acceptable_value = range(0,10) # value should lie from 0-10
    within_range=False

    # Condition that checks if the value provided is a digit or if the value lies in acceptable range
    #Executes once certainly due to initialization of variable above

    while my_gpa.isdigit() == False or within_range == False:
        #Accepts user input here
        my_gpa=input('Please enter your G.P.A (0-10): ')
        
        #If gpa is not a digit, display error message and continue accepting user input
        if my_gpa.isdigit() == False:
            print("The value you entered is not a digit, please try again!")
        
        if my_gpa.isdigit() == True:
            #If gpa is a digit, then checks if the value is acceptable else throws error message
            if (int(my_gpa) in acceptable_value) == False:
                within_range=False
                print("The value you entered is not in acceptable range, please try again!")
            else:
                within_range = True
                # If the value is acceptable, it further determines the grade 
                if int(my_gpa)>7:
                    print("You have received A Grade!")
                elif int(my_gpa)>4 and int(my_gpa)<8:
                    print("You have received B Grade!")
                else:
                    print("You have received C Grade!")

#Function call --> executed First
know_my_grade()