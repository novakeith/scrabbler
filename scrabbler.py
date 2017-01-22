# coding: UTF-8
# Scrabbler by KNOVA
# submitted as part of the reddit.com/r/dailyprogrammer challenge #294
# see here: https://www.reddit.com/r/dailyprogrammer/comments/5go843/20161205_challenge_294_easy_rack_management_1/

# scrabble letter values
ltrVal = {'?':0, 'a':1, 'b':3, 'c':3, 'd':2, 'e':1, 'f':4, 'g':2, 'h':4, 'i':1, 'j':8, 'k':5, 'l':1, 'm':3, 'n':1, 'o':1, 'p':3, 'q':10, 'r':1, 's':1, 't':1, 'u':1, 'v':4, 'w':4, 'x':8, 'y':4, 'z':10}

# returns a dictionary of the letters in a given word and the frequency of that letter
def countletters(words):
    newDict = {'?':0}
    for x in words:
        if x in newDict:
            newDict[x] = newDict[x] + 1
        else:
            newDict[x] = 1
    return newDict

# get the total scrabble value of a given word
def countwordval(word):
    pointval = 0
    for x in word:
        pointval += ltrVal[x]
    return pointval

# compare to see how many wildcards are needed to play A, given set of B letters
def wordcompare(letters, dicword):
    # cError is the distance between the two word dicts; devalue is the point loss due to that.
    cError = 0
    devalue = 0
    for z in dicword:
        if z in letters:
            if letters[z] >= dicword[z]:
                cError += 0
            else:
                cError += 1
                devalue += ltrVal[z]

        else:
            cError += 1
            devalue += ltrVal[z]

    return {'distance':cError, 'devalue':devalue}


def main():
    print "\n**Scrabble Finder v1.0\n" \
          "**Enter the letters you have and the word you want to play.\n" \
          "**This will tell you if you can play the word or not.\n" \
          "**Use a ? (question mark) for wildcard/blank tiles.\n"

    uLetters = raw_input("What letters do you have:>")

    uWord = raw_input("What word do you want to create?>")

    # count up letters in the letter list - using our shiny new function 'countletters'.
    wDict = countletters(uLetters)
    xDict = countletters(uWord)

    # lastly, compare the number of letters in the desired word to the count of the letter list
    # cError is the number of letters not matching; if the number of wildcards is equal or exceeds that number,
    #  the word is valid to be played
    comp = wordcompare(wDict,xDict)

    wildcards = comp['distance'] - wDict['?']


    # let the user know the good or bad news
    if wildcards <= 0:
        print "You can play that word! Point Value: " + str(countwordval(uWord) - comp['devalue'])
    else:
        print "Sorry, that word is not possible with your current letters.\n"
        print "Number of wildcards available: " + str(wDict['?']) + "\n"
        print "Number of additional wildcards needed: " + str(wildcards)

main()
