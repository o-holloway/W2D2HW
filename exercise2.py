#Create a list of names of 4 letters or more and capitalize each name
#Refactored to account for edge case, even if "name" is a 4-digit (or higher) number

names1 = ['connor', 'connor', 'bob', 'connor', 'evan', 'max', 'evan', 'bob', 'kevin']

def CapitalizeNamesWith4OrMoreChars(names1):
    capitalNames = []
    for name in names1:
        if len(str(name))>=4:
            capitalNames.append(str(name).capitalize())
    return capitalNames

print(CapitalizeNamesWith4OrMoreChars(names1))