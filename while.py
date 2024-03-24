#PSEUDOCODE

#Create a program that continually ask the user to enter a number
#If the user enters "-1", the program shoud stop requesting the user to enter a number.
#Calculate the the average of the numbers entered by the user excluding the "-1"

nums = []
num = 0

while num != -1: 
    
    num = int(input("Enter a number: "))
    print(f"You entered: {num}")
    if num != -1:
        # the append method keeps records of elements  of the user 's input in list 'nums'.
        nums.append(num)
        #calculate ans display the average 
        average = sum(nums)/len(nums)
        print(average) 
    #checks if the user's input was '-1', if so breaks and end the program
    elif num == -1:
        break
