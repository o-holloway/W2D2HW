##Write a program that takes in a user input and prints out how many vowels are in the response

# "Example" -> 3
# "Hello World" -> 3
# "Brian" -> 2
# "This is a longer response" -> 8

def howmanyvowels(usr_input):

    vowels = ['a','e','i','o','u']
    vowel_cnt = 0
    input_lower = []
    
    input_lower = [words.lower() for words in usr_input]
    
    for letter in input_lower:
        for vowel in vowels:
            if vowel == letter:
                vowel_cnt +=1
    
    print(vowel_cnt)

howmanyvowels("Example")
howmanyvowels("Hello World")
howmanyvowels("Brian")
howmanyvowels("This is a longer response")