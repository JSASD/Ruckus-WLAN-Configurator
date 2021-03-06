import random
import os
import logging

# Generates random 3-word phrases, "-" delimited
def createKey(__location__):
    """
    Creates guest key to set on WLANS

    ### Returns
    Randomly generated key
    
    ### Depends on
    None

    ### Parameters
     - __location__: str
       - Static location of main.py used for reliable file opening
    """
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

    logging.info("Key generated")
    logging.debug(key)
    return(key)