#apni dictionary
d1 = {"a":"apple",
      "b":"ball",
      "c":"cat",
      "d":"dog",
      "e":"elephant",
      "f":"fish",
      "g":"grape",
       "h":"hen",
      "i":"icecream",
      "j":"jam",
      "k":"kite",
      "l":"light",
      "m":"mouse",
      "n":"nest",
      "o":"owl",
      "p":"pea",
      "q":"queen",
      "r":"rat",
      "s":"stem",
      "t":"toy",
      "u":"umbrella",
      "v":"van",
      "w":"wax",
      "x":"x-mas",
      "y":"yak",
      "z":"zebra"
      }
print("Welcome to our dictionary")
print("Enter letter you want to learn about")
i1 = input()                    #getting input as string
print("You enter", i1)
print(i1 , "for" ,  d1[i1])
print("Do you want to search more?")
print("For yes type 'y' and for no type 'n' ")
i2 = input()
if  (i2 == "y" or i2 == "Y"  or i2 == "yes" or i2 == "Yes" or i2 == "YES"):
    print("Enter letter you want to learn about")
    i3 = input()  # getting input as string
    print("You enter", i3)
    print(d1[i3])
elif (i2 == "n" or i2 == "N"  or i2 == "no" or i2 == "NO" or i2 == "No"):
    print("Sad to listen! But thank you and visit again")
else:
    print("please enter a valid input")