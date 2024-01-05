import math

Location=["City Centre","Industrial Zone","Residential District","RuralOutskirts","Downtown"]
Radiation=[[22,19,20,31,38],[35,32,30,37,48],[15,12,18,20,14],[9,13,16,14,7],[25,18,22,21,26]]

sum=0
count=0
sum_square=0
variance=0

try:

 print("Location  -  Radiation\n")

 for i in range(len(Location)):
   
    val=Radiation[i]

    for j in val:
        sum+=j
        count=count+1

    avg=float(sum/count )

    print(f'{Location[i]}-----{Radiation[i]}\n')
    
    print(f"Average is:{avg}\n")  
    
    for i in val:
    
       deviation= i-avg 
       dev_square=deviation**2
       sum_square+=dev_square
    
    variance+=sum_square/len(Radiation)
    std_dev=math.sqrt(variance)

    print(f'Standard Deviation : {std_dev}\n')

except Exception as e:    

    print(e)