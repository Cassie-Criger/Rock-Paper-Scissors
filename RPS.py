#Cassandra Criger
#Rock Paper Scissors
#RPS.py
#added comment for github
import random

pScore = 0
cScore = 0
ties = 0
cMoves = ["rock", "paper", "scissors"]

print("Welcome to Rock Paper Scissors")
pName = input("What is your name?: ")

def printScore():
	print("Score: ")
	print(pName + ": " + str(pScore))
	print("Computer Score: " + str(cScore))
	print("Ties: " + str(ties))

while True:
	pMove = input("Enter 'r' for rock, 'p' for paper, 's' for scissors, or 'q' to quit")
	printScore()
	if pMove == "q":
		break
	cMove = random.choice(cMoves)
	if pMove == "r":
		print(pName + "picked Rock")
	    if cMove == "rock":
	    	print("Computer picks Rock")
	    	print("Tie")
	    	ties += 1
	    elif cMove == "paper":
	    	print("Computer picks Paper")
	    	print("Computer wins")
	    	cScore += 1
	    else cMove == "scissors":
	    	print("Computer picks Scissors")
	    	print("You won")
	    	pMove += 1
	elif pMove == "p":
		print(pName + "picked Paper")
	    if cMove == "paper":
	    	print("Computer picks Paper")
	    	print("Tie")
	    	ties += 1
	    elif cMove == "rock":
	    	print("Computer picks Rock")
	    	print("You wins")
	    	cScore += 1
	    else cMove == "scissors":
	    	print("Computer picks Scissors")
	    	print("Computer won")
	    	pMove += 1
	elif pMove == "s":
		print(pName + "picked Scissors")
	    if cMove == "scissors":
	    	print("Computer picks Scissors")
	    	print("Tie")
	    	ties += 1
	    elif cMove == "paper":
	    	print("Computer picks Paper")
	    	print("You wins")
	    	cScore += 1
	    else cMove == "rock":
	    	print("Computer picks Rock")
	    	print("Computer won")
	    	pMove += 1
	else:
		print("That is not an option")