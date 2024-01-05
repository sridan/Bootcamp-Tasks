#This is an example python program showing the use of math package and using sqrt().
#The user inputs 3 lengths of the triangle.
#The program outputs the Area of triangle using Heron's Formula.

import math

print("Enter the lengths of all three sides of a triangle:")

side1=float(input())
side2=float(input())
side3=float(input())

s=(side1+side2+side3)/2
x=s*(s-side1)*(s-side2)*(s-side3)
area=math.sqrt(x)

print(f"Area of triangle is:{area}")
