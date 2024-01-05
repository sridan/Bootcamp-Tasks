#This is an example python program of using for loop and if-else statement.
#The program outputs the specified star pattern.


count = 5
pattern="*"

print("\n")

for num in range(1, 10):

    if num > count:
        
        num=(count*2)-num
        print(pattern*num)
        print("\n")

    else:
        
        print(pattern*num)
        print("\n") 

