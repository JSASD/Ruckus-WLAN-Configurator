import random
import os

# Generates random 3-word phrases, "-" delimited
def createKey(__location__):
    # Open file 'wordList.txt'
    file = open(os.path.join(__location__,'wordList.txt'), 'r')
    # Read file line by line
    wordList = file.readlines()
    # Initialize list of words
    words = []
    # Add each word from wordlist into the 'words' list
    for line in wordList:
        words.append("{}".format(line.strip()))
    # Close the file
    file.close()
    # Number of words to be placed in phrase
    phraseSize = 2
    # Initialize list to place the phrase in
    phrase = []
    for i in range(phraseSize):
        phrase.append(words[random.randrange(1,len(words))])
    # Create key and store in variable
    key = '-'.join(str(x) for x in phrase)
    # Print the key
    return(key)