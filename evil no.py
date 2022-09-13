a = int(input("enter a number : "))
b = a**2
print()
list = []
for i in range(1,10):
    #print(f"i =  {i}")
    if b*10 >= (10**i):
        c = b%(10**i)
        #print(f"c =  {c}")
        d = (c*10)/(10**i)
        #print(f"d = {d}")
        e = b - c
        b = e
        list.append(d)
    elif i==0 :
        break
    else:
        pass
print(list)
list.reverse()
print(list)
print(list)