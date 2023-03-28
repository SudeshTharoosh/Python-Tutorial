##line = "   more white space   "
##print(line)
##print(line.strip())
##print(line)
##
##
##line = "   lots of white space   "
##print(line)
##line = line.strip()
##print(line)
##
##
###C. Finding data in strings
##guesses = "abcde"
##letter = "z"
##if letter in guesses:
##    print(letter)
##else:
##    print("_")



###D. Traversing a string
###Example 1
##name = "liz"
##for char in name:
##    print(char.upper()*3)
##
##
###Example 2
##message = "Testing"
##count = 0
##for character in message:
##    print(f'Index:{count}, Character:{character}')
##    count += 1



#E. Extended Exercise: Guess the word

turns = 6
secret = "water"
guesses = []
print("Let's play Guess the Word\nYou have 6 turns to guess the word!\n_ _ _ _ _\n")
while turns > 0:
    turns -= 1
    letter == input("\nGuess the letter: ")
    guesses = guesses + guess[0]
    for letter in secret:
        if letter in guesses:
            print('',letter,'',end='')
        else:
            print(' _ ',end='')
print("\nEnd of Game")
        
    

    
