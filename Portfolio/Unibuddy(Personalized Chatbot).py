try:
  student_name=input("Enter your name:")

  print(f'Welcome {student_name} on board. I hope you will have a amazing time here'+"\n")

  student_age=int(input("Enter your age:"))

  if student_age==18:

    print("Wow, you're starting university at a young age! You must be really talented."+"\n")

  elif student_age>25 and student_age<=35:

    print("Hmm, you're much older than I expected."+"\n")

  elif student_age>35:

    print("That's fantastic! It's never too late to learn and grow."+"\n")   

  else:

    print(f"{student_age} is a fun age to start university at!I started when I was 18 years old"+"\n")    
    
  student_fav_colour=input("Enter your favourite colour:")

  if student_fav_colour.lower()=="blue":

    if student_age<20:

        print('Join the Golf Club'+"\n")

    else:

        print("Join the swimming club"+"\n")  

  elif student_fav_colour.lower()=="red":

    print('Join the Dodge club'+"\n")

  elif student_fav_colour.lower()=="yellow":

    print('Join the Badminton club'+"\n")   

  else:

    print(f'Join the {student_fav_colour} Art club '+"\n")  
     
  questions=["Who can help me with my curriculum form?",
          "Where can I find out more about student accommodation?",
          "What clubs does the university offer?"] 
  
  answers=["You can contact the student support team they can help you with that.",
         "You can contact the university accomodation department they can guide you",
         "There are many clubs for sports and fitness which are available to see in the university website clubs"]
  
  for i in range(len(questions)):
      
          print(questions[i]+"\n"+answers[i]) 
          print("\n")              

  response=input(("Is there anything we could help you with ?")) 

  if response=='bye':
      
    print(f"It's nice talking to you {student_name}.Have a Good day!!") 
   
except Exception as e:
    print(e)
                 