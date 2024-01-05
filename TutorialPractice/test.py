message="hello world i am siri"
new_message=message.split()
for i in range(len(new_message)):
   if (i%2==0):
      temp=" "+new_message[i].upper()
      print(temp,end="")
   else:
       temp=" "+new_message[i]
       print(temp,end=" ")
    
