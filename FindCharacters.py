"""
Assignment: Find Characters
Write a program that takes a list of strings and a string containing a single
character, and prints a new list of all the strings containing that character.
"""

def FindCharacters(aListOfStrings, LookForChar):
    #we could use Reduce here, except we are not allowed.
    print "word_list = {0}".format(aListOfStrings)
    print "char = {0}".format(LookForChar)
    returnList = []
    for aWord in aListOfStrings:
        for ch in aWord:
            if (str(ch) == LookForChar) :
                returnList.append(aWord)
                break;
    print "new_list = {0}".format(returnList)

"""
Here's an example:
# input
word_list = ['hello','world','my','name','is','Anna']
char = 'o'
# output
new_list = ['hello','world']
"""

word_list = ['hello','world','my','name','is','Anna']
char = 'o'
FindCharacters(word_list, char)
