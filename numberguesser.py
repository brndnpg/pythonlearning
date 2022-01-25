import random

def numguess():
    guess = 0
    rnum = random.randrange(1,11)
    

    while guess != rnum:
        guess = int(input("I am thinking of a number between 1 and 10. Guess..."))
        if (guess > rnum):
                print("Too high! Try Again")
        if (guess < rnum):
                print("Too low! Try Again")
        elif (guess == rnum):
                print("Great Job! You guessed correctly")

numguess()