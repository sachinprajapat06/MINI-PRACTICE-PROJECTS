#print("printing star pattern")

print( "Welcome to our game")
print( "Here you can print your desirable pattern")
try:
    print("")
    print("START")
    print( "1. Type anything to normal pattern ")
    print("2. Leave blank for inverted")
    print("")
    p = bool(input("Pattern you want?"))
    print("")
    n = int(input("How much lines of pattern do u want?"))
    print(p)
    if(p == True):                                          #boolean answer will always be like True not true
        for i in range(0,n,+1):                         #for i in range (initial,final,iteration)
            for j in range(0,i+1):
                print("*", end="")
            print( "")
    elif(p == False):
        for i in range(n, 0, -1):
            for j in range(0, i, +1):
                print("*", end="")
            print("")

except Exception as e:                          # for encountering any problem error will get print but not ruin our program
    print(e)
    print("please put a valid number")