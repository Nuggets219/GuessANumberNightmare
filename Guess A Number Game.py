import random
global wins
global guesses
global maxNum
global rigged
wins = 0
guesses = 0
rigged = 0

def nightmareExplanation(): #explains the nightmare difficulty
    print("Let me explain the Nightmare difficulty:")
    print("There are 3 things that are changed just to make this difficulty more annoying.")
    print("When you guess:")
    print("Your guess can be randomly shifted up or down by 1, if RNJesus chooses so.")
    print("The correct number will randomly change, but it will be made known if it does so.")
    print("There is a 0.01% chance that the program just crashes on you.")
    print("If you guess higher than the correct answer, there is a chance the answer will blueshell you, increasing your number of guesses by 5 and changing the correct answer.")
    print("Good luck. Also, you will probably cry.")
def difficultySelect(): #difficulty selection screen
    global maxNum
    global rigged
    playerDecidedIfSure = 0
    print("difficulty menu:") #/n for line breaks didn't want to work :(
    print("0: Totally 100% the easiest difficulty! Not hard at all, I promise! (1-1000)")
    print("1. Sub-Brick (1-10) ")
    print("2. Below Average (1-50) ")
    print("3. Normal Human(1-100) ")
    print("4. Above Average (1-200)")
    print("5. NIGHTMARE! (Actually Rigged) (1-100)")
    print("Pick your difficulty. ")
    difficulty = input("")

    if difficulty == "0": #check the difficulties as stringss because i'm too lazy to check them as integers
        print("Difficulty is: Insanely Hard! I LIED! MWAHAHAHAHAHAHA!")
        maxNum = 1000
    elif difficulty == "1":
        print("Difficulty is: Sub-Brick! You should probably get that checked out.")
        maxNum = 10
    elif difficulty == "2":
        print("Difficulty is: Below Average! It doesn't matter too much, anyways.")
        maxNum = 50
    elif difficulty == "3":
        print("Difficulty is: Normal Human! Perfectly unremarkable!")
        maxNum = 100
    elif difficulty == "4":
        print("Difficulty is: Above Average! Look at Einstein over here!")
    elif difficulty == "5":
        print("Difficulty is... Actually Rigged. I'm not joking, this is actually rigged. Are you sure you want to do this?")
        while playerDecidedIfSure != 1: #are you sure you want to play Nightmare difficulty?
            nightmareConfirmation = input("Y/N")
            if nightmareConfirmation == "Y" or nightmareConfirmation == "y":
                print("your funeral.")
                maxNum = 100
                rigged = 1
                playerDecidedIfSure = 1
                nightmareExplanation()
            elif nightmareConfirmation == "N" or nightmareConfirmation == "n":
                print("good choice.")
                playerDecidedIfSure = 1
                difficultySelect()
            else:
                print("try that again, Y or N.")
    else:
        print("that's not a valid response. Try that again.")
        print("-------------------------")
        print("")
        difficultySelect()
def triviaQuestions ():
    if random.randint(1,100) <= 10:
        randomQuestion = random.randint(1,10)
        if randomQuestion == 1:
            print("placeholder for q1")
            correctAnswer = "pq1a"
        elif
def decideBlueShell():
    global guesses
    if random.randint(1,100) <= 10: #10% chance to blueshell
        print("the guess blueshelled you, and increased your number of guesses by 4!")
        print("number of guesses before: ", guesses)
        guesses =+ 4
        print("new number of guesses: ", guesses)
def randomizeNumber(): #randomizes the correct number when called
    global randomNumber
    global maxNum
    if randomNumber != -1:
        print("Correct Number has changed!")
    randomNumber = random.randint(1, maxNum)
def decideGuessShift():
    if random.randint(1,20) == random.randint(1,20):
        shiftDirection = random.randint(1,2)
        if shiftDirection == 1:
            print("guess shifted down by 1")
            guess =- 1
        elif shiftDirection == 2:
            print("guess shifted up by 1")
            guess =+ 1
        else:
            print("error in decideGuessShift. Restart the program.")
def startGame(maxNum, rigged):
    global guesses
    global randomNumber
    randomNumber = -1 #setup so it doesn't print that the number changed on first number set.
    randomizeNumber()
    playAgain = "E" #sets the playagain string to an impossible value so it isn't called accidentally
    guess = 0  #guess is an unobtainable value to prevent unexpected errors
    print("i'm thinking of a number between 1 and", maxNum)
    print("guess a number")
    while guess != randomNumber: #standard while loop
        guesses += 1
        guess = int(input("guess: "))
        if rigged == 1: #Everything in this if block assists the Nightmare mode. not everything for the nightmare mode is in this block
            decideGuessShift()
            if random.randint(1,10) == 1: #Randomly randomize the number, 1 in 10 chance
                print("number has been randomized!")
                randomizeNumber()
            if random.randint(1,1000) == 1:  #1 in 1000 chance to crash
                print("1 in 1000 chance to crash, and you rolled a nat -13")
                int("you should crash the program NOW")
        if guess > maxNum or guess < 1: #handles the invalid numbers in a more easy to see way, at least for me
            print("what are you doing? That is NOT a number from 1-",maxNum,". That counts as a guess, and serves you right!")
        elif guess > randomNumber: #checks if the randomnumber is higher than the guess
            print("guess lower")
            if rigged == 1:
                decideBlueShell() #decides if the number blueshells you
        elif guess < randomNumber: #is it lower than its suppposed to be?
            print("guess higher")
        else:
            print("ultrarare error! quit the program and reflect on the decisions that brought you here.")

    print("correct! you win!")
    #add a win, print the number of wins
    wins =+ 1
    print("wins:", wins)
    #prints the guesses
    print("guesses:", guesses)
    acceptableEndInput = 0
    while acceptableEndInput == 0: #handles the decision to play again, with lowercase support and catching for invalid inputs.
        playAgain = input("play again? Y/N  ")
        if playAgain == "Y":
            startGame(maxNum, rigged)
            acceptableEndInput = 1
        elif playAgain == "y":
            startGame(maxNum, rigged)
            acceptableEndInput = 1
        elif playAgain == "N":
            print("bye!")
            acceptableEndInput = 1
        elif playAgain == "n":
            print("bye!")
            acceptableEndInput = 1
        else:
            print("That's... not Y or N.")

difficultySelect()
startGame(maxNum, rigged)