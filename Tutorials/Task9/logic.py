# This is an example python program demonstrating logical error.
# This program outputs the logical error.
# To Return the count of a given substring from a string.

count=0
string="Hello World I like to code and code and code ..."
sub_str="code"

try:
 
 str=string.split()
 print(str)
 
 for i in range(len(str)):
     
    if str[i]!=sub_str: #This logical error occurs because of using the wrong comparision operator
    
        count+=1

 print(f"Number of times the given substring appeared in the string is :{count}")   
      
except Exception as e:
  
     print(e)