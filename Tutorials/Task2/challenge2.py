#This is an example python program showing that string to int type casting is not possible.
#The user inputs his favourite restaurant name and  his favourite number.
#This program outputs the user's favourite restaurant and number and throws an error for string to int type casting.

string_fav=input("Enter your favourite restaurant:")

int_fav=int(input("Enter your favourite number:"))

print(string_fav)
print(int_fav)

print(int(string_fav))

#Displays the following Error:

#valueError:Invalid literal for int() with base 10.
#This is the error because we are trying to convert the user's favourite restaurant to integer type.
# using type casting which will throw an error as we cannot convert the string datatype to integer type unless
# the given input is an integer.This is because in python by defalut the input is considered as string type.
