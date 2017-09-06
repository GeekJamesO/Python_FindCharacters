# input
word_list = ['hello','world','my','name','is','Anna']
char = 'o'
# expected output

new_list = ['hello','world']

def FindCharacters(word_list, char):
    print "Word list:", word_list, "  Character: ", char
    rtnarray = []
    for aWord in word_list:
        for chars in aWord:
            if chars == char:
                rtnarray.append(aWord)
                break;
    return rtnarray
actualReturn = FindCharacters(word_list, char)
print "Expected Output", new_list
print "  Actual Output", actualReturn
