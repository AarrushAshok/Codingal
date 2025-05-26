#Number Guessing Game
import random
print("Welcome to number guessing game!!!!")
computerChoice = random.randint(1,100)

while True:
    userGuess = int(input("Enter your guessed number:"))
    if userGuess == computerChoice:
        print("You Won!!!")
    elif userGuess > computerChoice:
        print("Number is big. Keep guessing")
    elif userGuess < computerChoice:
        print("Number is small.Keep guessing")