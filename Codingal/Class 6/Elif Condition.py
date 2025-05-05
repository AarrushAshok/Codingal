#Elif Condition
print ("Welcome to the quiz game")
Score = 0

#Question 1
print("Question1 - Who is the PM of India?")
print("1.Narendra Modi")
print("2.Rahul Gandhi")
print("3.Stalin")
print("4.Jawaharlal Nehru")
Answer = int(input("Answer for Question1:"))
if Answer == 1:
    print("Correct Answer!")
    Score+=10
elif Answer == 2:
    print("Wrong Answer")
    Score-=5
elif Answer == 3:
    print("Wrong Answer")
    Score-=5
elif Answer == 4:
    print("Wrong Answer")
    Score-=5
else :
    print("Invalid")

#Question 2
print("Question2 - What is the National Bird of India?")
print("1.Crow")
print("2.Peacock")
print("3.Parrot")
print("4.Sparrow")
Answer = int(input("Answer for Question2:"))
if Answer == 1:
    print("Wrong Answer!")
    Score-=5
elif Answer == 2:
    print("Correct Answer!")
    Score+=5
elif Answer == 3:
    print("Wrong Answer")
    Score-=5
elif Answer == 4:
    print("Wrong Answer")
    Score-=5
else :
    print("Invalid")

#Question 3
print("Question3 - What is the National Animal of India?")
print("1.Lion")
print("2.Tiger")
print("3.Cow")
print("4.Elephant")
Answer = int(input("Answer for Question3:"))
if Answer == 1:
    print("Wrong Answer!")
    Score-=5
elif Answer == 2:
    print("Correct Answer!")
    Score+=5
elif Answer == 3:
    print("Wrong Answer")
    Score-=5
elif Answer == 4:
    print("Wrong Answer")
    Score-=5
else :
    print("Invalid")

#Question 4
print("Question4 - What is the Capital of India?")
print("1.Mumbai")
print("2.Delhi")
print("3.Chennai")
print("4.Kolkata")
Answer = int(input("Answer for Question4:"))
if Answer == 1:
    print("Wrong Answer!")
    Score-=5
elif Answer == 2:
    print("Correct Answer!")
    Score+=5
elif Answer == 3:
    print("Wrong Answer")
    Score-=5
elif Answer == 4:
    print("Wrong Answer")
    Score-=5
else :
    print("Invalid")

#Question 5
print("Question5 - Which planet is known as the Red Planet?")
print("1.Mars")
print("2.Earth")
print("3.Saturn")
print("4.Jupiter")
Answer = int(input("Answer for Question1:"))
if Answer == 1:
    print("Correct Answer!")
    Score+=5
elif Answer == 2:
    print("Wrong Answer")
    Score-=5
elif Answer == 3:
    print("Wrong Answer")
    Score-=5
elif Answer == 4:
    print("Wrong Answer")
    Score-=5
else :
    print("Invalid")

if Score <0: print("You Lost,Try Again")
else: print("Score:",Score)