# This example program is meant to demonstrate errors.
 
# There are some errors in this program. Run the program, look at the error messages, and find and fix the errors.

print ("Welcome to the error program")
print ("\n")

# Variables declaring the user's age, casting the str to an int, and printing the result
age = '24'
print(f"I'm {age} years old")

# Variables declaring additional years and printing the total years of age
years_from_now = "3"
new_age=int(age)+int(years_from_now)
total_years = new_age

print(f"The total number of years:{total_years}")

# Variable to calculate the total amount of months from the total amount of years and printing the result
total_months = (total_years * 12)
total_months+=6

print(f"In 3 years and 6 months, I'll be {total_months} months old")

#HINT, 330 months is the correct answer


