#faulty calculator

print("hello welcome to our calculator")
print("please enter your first no")
no1 = input()
print("please select an operator (+,-,*,/,%)")
op = input()
print("please enter your second no")
no2 = input()

if (op=="+" or op=="*" or op=="-" or op=="/" or op=="%"):
    if (no1=="45" and op=="*" and no2=="3"):
        print("answer= 555")
    elif (no1=="56" and op=="+" and no2=="9"):
        print("answer= 77")
    elif (no1=="56" and op=="/" and no2=="4"):
        print("answer= 4")
    elif (op == "+"):
        ans = no1 + no2
        print("ans")
    elif (op == "+"):
        ans = no1 + no2
        print("ans")
    elif (op == "-"):
        ans = no1 - no2
        print("ans")
    elif (op == "*"):
        ans = no1 * no2
        print("ans")
    elif (op == "/"):
        ans = no1 / no2
        print("ans")
    elif (op == "%"):
        ans = no1 % no2
        print("ans")
else:
    print("please put a valid operator and try again")
