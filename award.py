

#PSeudocode
#Design a program that determines the award a person recieves in a triathlon event
#Ask the user to enter the time for each exercise  (swimming, biking and running)
#Store the user's input in their corresponding variables "time_swim", "time_bike" and "run_time".
#Calculate and display the total time taken to complete the triathlon
#Compare the total time taken by the athlete to finish the triathlon with the time range to determine if they are within the qualifying criteria.
#Display the award the athlete  receives based on the following criteria:
 

swim_time = float(input("Enter swim time in minutes: "))
cycling_time = float(input("Enter bike time in minutes: "))
run_time = float(input("Enter run time in minutes: "))


#Sum the time taken for each event by the athlete and return a value 
def  triathlon_event(swim_time, cycling_time, run_time):
    """This is a function that calculates and return the total amount of time used to finish the triathlon event"""
    return swim_time + cycling_time + run_time



#Call the function and store the value  in variable "total_time"
total_time = triathlon_event(swim_time, cycling_time, run_time)
print(total_time)


def corresponding_award(total_time):

    """This function compares the total_time used to 
    complete in the triathlon event and the Time range
    """
    if total_time <= 100:
        return "Provincial colour"
    
    elif total_time >= 101 and total_time <= 105:
        return "Provincial half colour"
    elif total_time >= 106 and total_time <= 110:
        return "provincial scroll"
       
    elif  total_time > 111:
        return "No awards"
    else:
        print("Your coming makes a difference")


#Store the return value of the function to the variable  "award"
award = corresponding_award(total_time)

#display award won by the athlete base on their perfomance.
print(f"Congratulations, you have won {award}")
# print("You came second place with the {}.".format(award))
# print("Thanks for participating, you have the provincial scroll")
