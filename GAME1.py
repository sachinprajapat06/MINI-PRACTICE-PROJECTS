#STONE PAPER SISSOR GAME
import random

print("Welcome to our game")
print("You have to chose an option as stone paper sissor and computer will also choose the same! lets see who win")

score1 = 0
score2 = 0

chances = 1    #initialising value of i
while(chances<11):  #while loop for infinity
        user = input("Choose one and enter as {stone} or {paper} or {sissor}")
        if user=="stone" or user=="paper" or user=="sissor" :
            print("You choose : "+ user )
            options = ["stone", "paper", "sissor"]
            computer = random.choice(options)
            print("Computer chooses : " + computer)
            if user=="stone" and computer=="stone":
                    print("Draw")
                    score1 += 1
                    score2 += 1
                    chances += 1
            elif user=="paper" and computer=="paper":
                    print("Draw")
                    score1 += 1
                    score2 += 1
                    chances += 1
            elif user=="sissor" and computer=="sissor":
                    print("Draw")
                    score1 += 1
                    score2 += 1
                    chances += 1
            elif user=="paper" and computer=="stone":
                    print("User win")
                    score1 += 1
                    chances += 1
            elif user=="paper" and computer=="sissor":
                    print("Computer win")
                    score2 += 1
                    chances += 1
            elif user=="sissor" and computer=="stone":
                    print("Computer win")
                    score2 += 1
                    chances += 1
            elif user=="sissor" and computer=="paper":
                    print("User win")
                    score1 += 1
                    chances += 1
            elif user=="stone" and computer=="sissor":
                    print("User win")
                    score1 += 1
                    chances += 1
            elif user=="stone" and computer=="paper":
                    print("Computer win")
                    score2 += 1
                    chances += 1
        else:
            print("Please choose a valid input! and choose again" )

print("Game end ")
print("Results are" )
print("User get :" + str(score1))
print("Computer get :" + str(score2))
if score1>score2:
    print("User wins with a total of : " + str(score1) + " points")
elif score2>score1:
    print("Computer wins with a total of : " + str(score2) + " points")
elif score1==score2:
    print("Match draw")



