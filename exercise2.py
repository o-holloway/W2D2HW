#Create a list of names of 4 letters or more and capitalize each name
#*Double Bonus* Do it using list comprehension

names1 = ['connor', 'connor', 'bob', 'connor', 'evan', 'max', 'evan', 'bob', 'kevin']

def CapitalizeNamesWith4OrMoreChars(names1):
    capitalNames = []
    for name in names1:
        if len(name)>=4:
            capitalNames.append(name.capitalize())
    return capitalNames

print(CapitalizeNamesWith4OrMoreChars(names1))