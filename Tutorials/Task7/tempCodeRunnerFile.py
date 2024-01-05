#This is an example Python program of using while loop , if-else statements and try-except.
#The user inputs the number until the number matches -1.
#The output gives the Average of all the numbers entered excluding -1.

total=0
count=0

while True:
  
   num=input("Enter a number:")
   if not num.isdecimal() and not num.isnumeric():
         print('Please enter only numbers...')
         break 

   if(num!=-1):
     num=float(num)
     total=total+num
     count+=1
   else:
         break
   

avg_num=total/count
 
print(f" Average of the numbers entered excluding -1 : {avg_num}")    
