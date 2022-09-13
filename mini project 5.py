#fibonachi numbers
#logic is 0,1,1,2,3,5,8,13...
#start with 0,1 then new no will bw addition of last 2 no

print("start")

try:
    def f(n):               #we defined a funtion
        if n==1:            #fist term as 0
            return 0
        elif n==2:          #second term as 1
            return 1
        elif n==3:          #third term as 1
            return 1
        else:
            return f(n-1) +f(n-2)           #any term= sum of previous 2 terms
        #suppose we will try as 5 then n=5
        #f(5) = f(4) + f(3)
        #f(5) = (f(3) + f(2))+ (f(2) + f(1))
        # f(5) = ((f(2) + f(1)) + f(1))+ (f(2) + f(1))
        # f(5) = (1 + 1 + 1+ 1 + 1)


except Exception as e:                          #for encountering any problem error will get print but not ruin our program
    print(e)
    print("please put a valid number")

n = int(input("Please enter the no of digit you want?"))        #taking input by the user
print(f(n))             #direct printing the funtion but it also call f(n) then run it as with value of n given by the user