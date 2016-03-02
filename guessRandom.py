#Demonstration of binary search algorithm, but instead of the computer searching for a matching value, you get to look for it.

import random

maxGuess = 100
minGuess = 1
correctNum = random.randint(1,100)

print "Guess a whole number between 1 and 100"

myGuess = int(raw_input("> "))

while myGuess != correctNum:
	if myGuess > correctNum:
		maxGuess = myGuess - 1
		print "Your guess was too high."
		print "Guess a new number between %d and %d" %(minGuess, maxGuess)
		myGuess = int(raw_input("> "))
	else:
		minGuess = myGuess + 1
		print "Your guess was too low."
		print "Guess a new number between %d and %d" %(minGuess, maxGuess)
		myGuess = int(raw_input("> "))

print "That's it. The correct number was %d" %correctNum
