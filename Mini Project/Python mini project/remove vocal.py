# This program remove the vocal in the word
# Prompt the user to enter a word
# and assign it to the userWord variable.

userWord = input("Enter your word = ")
userWord = userWord.upper()

vocal = ("A","E","I","O","U")

for letter in userWord:
    
    if letter in vocal :
        continue
    print(letter)
    
