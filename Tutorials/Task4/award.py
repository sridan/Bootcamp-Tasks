#This is an example python program using if-elif-else statement and logical operators.
#The user inputs the time taken for swimming,cycling and running.
#calculates the triathlon and displays the result.
#The program outputs the award based on the qualifying time range of the triathlon .

swimming_time=int(input("Enter the time taken for swimming in minutes: "))
cycling_time=int(input("Enter the time taken for cycling in minutes:"))
running_time=int(input("enter the time taken for running in minutes:"))

triathlon_time=swimming_time+cycling_time+running_time

print(f"Total time taken to complete the triathlon:{triathlon_time}")

qualifying_time=100

if triathlon_time>=0 and triathlon_time<=qualifying_time:
   print("Congratulations you have been awarded Provincial Colours")
   
elif triathlon_time>=qualifying_time-5 and triathlon_time<=qualifying_time+5:    
    print("Congratulations you have been awarded Provincial Half Colours")   

elif triathlon_time>=qualifying_time-10 and triathlon_time<=qualifying_time+10:   
    print("Congratulations you have been awarded Provincial Scroll")  

else:
     print("No award")     
