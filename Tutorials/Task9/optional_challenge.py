# This is an example python program to demonstrate 2 compilation errors,a runtime error and a logical error
# using try-except.

# This is an example to demonstrate the first compilation error.
# To Print characters from a string that are present at an even index number.

try:

 string="Hello World"
    
 for i in range(0:len(string):2):#This compilation error occurs because of invalid syntax use of ':' instead of ','in range function.

   print(string[i])
        
except Exception as e:
  
   print(e)   
 #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  

# This is an example to demonstrate the second compilation error.
# To Remove first n characters from a string.
   
try:
       
  num=int(input("Enter the number:"))
  
  print(string(num:))#This compilation error occurs because of invalid syntax use of () instead of [] while slicing the string.
   
except Exception as e:
  
   print(e)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~   

# This is an example to demonstrate the runtime error.
# Check if the first and last character of a string matches and then concatenate 1 to the string.

try:
     
 string="Hello world"
 
 for i in range(len(string)):
    
     if string[i]==string[-1]:
       
         string+=1 #This Run time error occurs because of concatenating the string and int
    
     else:
       
         print(string[i],end=" ") 
            
 print('\n')
       
except Exception as e:
  
   print(e)
   
   #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# This is an example to demonstrate the logical error.
# Display the sum of first 5 numbers and display the result.
 
try:
    
 lst_sum=0
 
 for i in range(5): #This logical error occurs because of wrong index as the index '5' is not included.
    
     lst_sum=i+lst_sum
 
 print(lst_sum)
 
        
except Exception as e:
  
   print(e)
   
   