
print("welcome to our calculator")
def ask():
    print("what do you like to have ")
    dict = {1: 'arthematic progression', 2: 'geometric progressin', 3: 'simple interest', 4: 'compound interest', 5: 'investment plan', 6: 'evil number'}
    print(dict.items())
    a = int(input("choose a number to perform action :"))
    if(a==1):
        print("\n******arthematic progression******")
        ap()
    elif (a == 2):
        print("\n******geometric progression******")
        gp()
    elif (a == 3):
        print("\n******simple interest******")
        si()
    elif (a == 4):
        print("\n******compound interest******")
        ci()
    elif (a == 5):
        print("\n******investment plan******")
        pol()
    elif (a == 6):
        print("\n******evil number******")
        evil_number()
    else:
        print("\nplease enter a valid input")
        print("\033[H\033[J")
        ask()
def ap():
    pass
def gp():
    pass
def si():
    def siask():
        if (v=="y"):
            si()
        elif (v=="n"):
            d = input("\ndo you want to calculate something other \npress y for 'yes' and press n for 'no' \n enter:")
            if (d=="y"):
                ask()
            else:
                print("\n*********thank you*********")
        else:
            print("\nenter a valid input")
            siask()
    def siask1():
        x = input("Is your rate \n1. 'per year press : y' \n2. 'per month press : m' \n :")
        if (x == "y"):
            t = int(input("enter number of years : "))
            x = "years"
            return t, x;
        elif (x == "m"):
            t = int(input("enter number of months : "))
            print(f"{t} months or {t/12} years")
            x = "months"
            return t, x;
        else:
            siask1()
    t, x = siask1()
    p = int(input("enter your base amount 'principle' : "))
    r = int(input("enter your rate of interest 'rate' : "))

    a = (p*r*t/100)+p
    l = a-p
    print(f"only intrest is {l} ")
    print(f"your final amount is {a}\nwith principle: {p}  rate: {r}  time: {t} {x} \n")
    v = input("\ndo you want to calculate it again \npress y for 'yes' and press n for 'no' \n enter:")
    siask()
def ci():
    def ciask():
        if (v == "y"):
            si()
        elif (v == "n"):
            d = input("do you want to calculate something other \npress y for 'yes' and press n for 'no' \n enter:")
            if (d=="y"):
                ask()
            else:
                print("\n*********thank you*********")
        else:
            print("enter a valid input")
            ciask()

    def ciask1():
        x = input("Is your rate \n1. 'per year press : y' \n2. 'per month press : m' \n :")
        if (x == "y"):
            t = int(input("enter number of years : "))
            x = "years"
            return t, x;
        elif (x == "m"):
            t = int(input("enter number of months : "))
            print(f"{t} months or {t / 12} years")
            x = "months"
            return t, x;
        else:
            ciask1()

    t, x = ciask1()
    p = int(input("enter your base amount 'principle' : "))
    r = int(input("enter your rate of interest 'rate' : "))

    a = p*((100+r)/100)**t
    l = a - p
    print(f"only intrest is {l} ")
    print(f"your final amount is {a}\nwith principle: {p}  rate: {r}  time: {t} {x} \n")
    v = input("\ndo you want to calculate it again \npress y for 'yes' and press n for 'no' \n enter:")
    ciask()
def pol():
    def polask():
        if (v=="y"):
            pol()
        elif (v=="n"):
            d = input("\ndo you want to calculate something other \npress y for 'yes' and press n for 'no' \n enter:")
            if (d=="y"):
                ask()
            else:
                print("\n*********thank you*********")
        else:
            print("\nenter a valid input")
            polask()
    def polask1():
        x = input("Is your rate \n1. 'per year press : y' \n2. 'per month press : m' \n :")
        if (x == "y"):
            t = int(input("enter number of years : "))
            x = "years"
            return t, x;
        elif (x == "m"):
            t = int(input("enter number of months : "))
            print(f"{t} months or {t/12} years")
            x = "months"
            return t, x;
        else:
            polask1()
    p = int(input("enter your base amount you want to invest per month or year 'principle' : "))
    r = float(input("enter your rate of interest 'rate' : "))
    t, x = polask1()
    k = p
    y = p
    z = 1
    while z <= t:
        pr = y*r/100
        k = pr + y
        y = k + p
        print(f"after {z} {x} your profit is: {pr} and overall value is: {y}")
        z += 1
    v = y - p
    l = v - (p*t)
    inv = p*t
    print(f"only intrest is : {l} ")
    print(f"you only invested : {inv}")
    print(f"your final amount is : {v}\nwith principle : {p}  \nrate : {r}  \ntime : {t} {x} \n")
    v = input("\ndo you want to calculate it again \npress y for 'yes' and press n for 'no' \n enter:")
    polask()
def evil_number():
    def evask():
        if (v == "y"):
            evil_number()
        elif (v == "n"):
            d = input("do you want to calculate something other \npress y for 'yes' and press n for 'no' \n enter:")
            if (d=="y"):
                ask()
            else:
                print("\n*********thank you*********")
        else:
            print("enter a valid input")
            evask()

    num = int(input("enter your no : "))
    a = num
    b = a ** 0.5
    g = 0
    c = int(round(b, 0))
    # print(c)
    for d in range(c, -1, -1):
        e = 2 ** d
        if a >= e:
            f = (a - e)
            a = f
            # print(f" it return a 1 ")
            g += 1
            # print(f" g became {g}")
        elif a <= e:
            pass
            # print(f" it return 0 ")
            # print(f" g became {g}")
        elif a == 0:
            pass
            # print(f" g became {g}")
            break
    if g % 2 == 0:
        print(f" {num} is an evil number as binary value of {num} have {g} (even number) of 1's ")
    else:
        print(f" {num} is not an evil number as binary value of {num} have {g} (odd number) of 1's ")
    v = input("\ndo you want to calculate it again \npress y for 'yes' and press n for 'no' \n enter:")
    evask()


ask()
