#This is an example Python program showing the string manipulations using slicing and string methods.
#The user inputs the sentence and displays the length of the string as output.
#The program outputs the sentence with the specified manipulations.

str_manip = input("Enter a sentence:")
print(f"The Length of the entered string is:{ len(str_manip) }")

last_char = str_manip[-1]

str_manip_rep = str_manip.replace(last_char,'@')
print(str_manip_rep)

str_manip_last3 = str_manip[:-4:-1]
print(str_manip_last3)

str_manip_new_word = str_manip[0:3]+str_manip[-2::]
print(str_manip_new_word) 