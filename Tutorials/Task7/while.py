#This is an example Python program of using while loop , if-else statements.
#The user inputs the number until the number matches -1.
#The output gives the Average of all the numbers entered excluding -1.

total=0
count=0

while True:
    num=input("Enter any number:")
    
    if num.isalpha():
        
        print("Please enter only numbers...\n")
        break
    
    if num!="-1":
        
        num=float(num)
        total+=num
        count+=1
        
    else:
        
        break  
          
avg_num=total/count

print(f"Average of all the numbers excluding '-1' is:{avg_num}")