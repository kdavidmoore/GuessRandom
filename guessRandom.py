# Instructions from: https://www.daniweb.com/programming/software-development/threads/131973/5-crucial-projects-for-beginners
# Instructions: The computer randomly generates a number. The user inputs a number, and the computer will tell you if you are too high, or too low. Then you will get to keep guessing until you guess the number.
# My solution is as follows...
import random

while True:
    try:
        print "Welcome to the randum number guessing game."
        low = int(raw_input("Enter a lower bound (must be an integer) > "))
        high = int(raw_input("Now enter an upper bound (must be an integer) > "))
        break
    except ValueError:
        print "You did something wrong..."
      
rand = random.randint(low,high)
guess = rand + 1

while True:
    try:
        while rand != guess:
            guess = int(raw_input("Make your guess > "))
            if guess > rand:
                print "Your guess is too high. Try again.\n"
            elif guess < rand:
                print "Your guess is too low. Try again.\n"
            elif guess == rand:
                print "You got it right!"
            else:
                print "Something went wrong..."
        break
    except ValueError:
        print "That's not an integer..."
