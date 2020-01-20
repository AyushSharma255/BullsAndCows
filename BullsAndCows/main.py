from helper import *

def playGame():
    randomNum = genNum()
    run = True

    while run:
        guessNum = int(input("Guess the number with no duplicates: "))

        if isUnique(guessNum) == False:
            pass
        elif len(guessNum) != 3:
            pass

        cows, bulls = giveCowsAndBulls(randomNum, guessNum)

        print(f"You had {cows} cows and {bulls} bulls.")

        if bulls == 3:
            print("You've won!")
            won = False
            choice = input("Would you like to play again? [y/n]")

            if choice == "y":
                playGame()


playGame()