#This is an example Python program showing if-elif-else statements.
#The user inputs their age.
#The program outputs the message based on their age.

age=int(input("Enter your age:"))

if age>100:
    print("Sorry,you're dead.")

elif age>=40:
    if age>=65:
             print("Enjoy your retirement!") 
    else:
             print("You're over the hill.")

elif age==21:
     print("Congrats on your 21st!")

elif  age<13: 
     print("You qualify for the kiddie discount.")

else:
    print("Age is but a number.")          
    
    