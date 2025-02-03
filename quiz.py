print("WELCOME TO THE GAME")
print("Hello Sir")
playing = input("Do you want to play? ")
if playing.lower() != "yes":
  print("OKAY, GOODBYE!")
  quit()
print("Okay, Let's see how much hunger do you have")
score = 0
answer = input("What does ALU stand for? ")
if answer.lower() == "arithmetic logic unit":
  print("You are correct")
  score += 1
else:
  print("Incorrect")

answer2 = input("What does CPU stand for? ")
if answer2.lower() == "central processing unit":
  print("You are correct")
  score += 1
else:
  print("Incorrect")
answer3 = input("What does GPU stand for? ")
if answer3.lower() == "graphical processing unit":
  print("You are correct")
  score += 1
else:
  print("Incorrect")
answer4 = input("What does RAM stand for? ")
if answer4.lower() == "random access memory":
  print("You are correct")
  score += 1
else:
  print("Incorrect")

print("You have answered all the questions")
print("Total Correct answers are:", score)
print("Total percentage: ", str((score/4)*100))
