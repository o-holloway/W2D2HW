# Bonus Challenge - Create a list of names of 4 letters or more and capitalize each name
# using list comprehension

# Edge case: Coded to eliminate error even if "name" is a 4-digit (or higher) number

names2 = ['connor', 'connor', 'bob', 'connor', 'evan', 'max', 'evan', 2, 2, 2, 3, 3, 4, 'bob', 'kevin']

def CapitalizeNamesWith4OrMoreChars(names2):
    capitalNames2 = []
    capitalNames2 = [str(name).capitalize() for name in names2 if len(str(name))>=4]

    return capitalNames2

print(CapitalizeNamesWith4OrMoreChars(names2))