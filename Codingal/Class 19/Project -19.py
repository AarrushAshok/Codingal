#Number Guessing Game
import random
print("Welcome to number guessing game!!!!")
print("Max number of attempts will be 5!!")

def playGame():
    computerChoice = random.randint(1,100)
    maxAttempts = 5
    attempts = 0
    while attempts < maxAttempts:
        userGuess = int(input("Enter your guessed number between 1 to 100:"))
        attempts += 1
        if userGuess == computerChoice:
            print("You Won!!!")
            break
        elif userGuess > computerChoice:
            print("Number is big. Keep guessing")
        elif userGuess < computerChoice:
            print("Number is small.Keep guessing")

    if attempts == maxAttempts and userGuess != computerChoice:
        print("You've used all attempts! The number was:",computerChoice)
        print("Good Luck next time!")

while True:
    print("1.Play Game")
    print("2.End Game")
    choice = int(input("Enter your choice:"))
    attemnpts = 0
    if choice == 1:
        playGame()
    if choice == 2:
        print("Thank You, Come back Soon!!")
        break