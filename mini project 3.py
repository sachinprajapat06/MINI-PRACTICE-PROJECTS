print("Welcome to the no game")
print("now you have to guess a no between 0 to 100 with a limited no of guesses 5")
x = 5                   #initialize our chances as x=5
while(True):        #never stopping while loop
    i1 = int(input())           #getting input
    if i1==67:                  #checking condition
        print("congrats you won with " ,x ," chances left")
        break                   #end program because user won
    elif i1<67:                 #checking condition
        print("the no must be greater")
    elif i1>67:                 #checking condition
        print("the no must be smaller")
    x = x - 1                   #out of our conditons and updating left chances
    print("sorry your answer is wrong but you have " ,x ," chances left")
    if x==0:                    #if left chances become 0
        print("you lost with 0 chances left")
        break                   #you lose and loop end
