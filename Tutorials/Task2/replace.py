#This is an example Python Program showing the string methods :replace(),Upper() and slicing.
#The message assigned to the variable.
#The program outputs the required message by removing the '!' marks and replacing with blank space
#and also displays the message in upper case.Also outputs the message in reverse order using slicing.

message="The!quick!brown!fox!jumps!over!the!lazy!dog."

message_rep=message.replace("!"," ")
print(message_rep)

message_upp=message_rep.upper()
print(message_upp)

message_rev=message_upp[::-1]
print(message_rev)