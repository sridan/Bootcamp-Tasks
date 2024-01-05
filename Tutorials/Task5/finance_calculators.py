#This is a Capstone Project that allows the user to access two different financial calculators:an investment calculator 
# and a home loan repayment calculator.
#The user inputs the selection whether to choose investment or bond according to his preference.
#if the user chooses investment then it calculates the total amount including interest depending 
# on the choice of simple interest or compound interest.
#if the user chooses bond then it calculates the home loan monthly repayment amount.

import math
print("\ninvestment - to calculate the amount of interest you'll earn on your investment")
print("bond - to calculate the amount you'll have to pay on a home loan\n")
 
while True:
    
   question=input("Enter either-'investment' or 'bond' from the menu above to proceed:")
   question=question.lower()
   question=question.strip()
   

   
   if((question=="investment")):
   
    P=float(input("\nEnter the amount to be deposited:"))
    r=float(input("Enter the Interest rate:"))
    r/=100
    t=float(input("Enter the Number of years you are planning to invest in:"))
    interest=input("\nDo you want simple interest or compound interest:")
    interest=interest.lower()
    interest=interest.strip()
   
    if (interest=="simple interest"):
      
       A=float(P*(1+r*t))
       #print(A)
       print(f"\nTotal amount after the interest applied:{A}")
       break
   
    elif(interest=="compound interest"):

         A=float(P*math.pow((1+r/100),t))
         print(f"\nTotal amount after the interest applied:{A}")
         break
   
    else:
    
      print("\nEnter either simple interest or compound interest:")   
      break
   
   elif((question=="bond")):
    
      P=float(input("\nEnter the value of the house:"))
      i=float(input("Enter the rate of interest:"))
      i/=100
      i/=12
      n=int(input("Enter the number of months to repay your bond:"))
      x=(1-(math.pow((1+i),(-n))))
      repayment=(i*P)/x
      
      print(f"\nMonthly Repayment for the Home loan is:{repayment}\n")
      break
   
   else:        
   
      print("\nEnter the valid input please enter Investment or Bond\n")
      
      