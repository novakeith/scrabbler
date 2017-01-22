# coding: UTF-8
# Scrabbler by KNOVA -- v1.3
# submitted as part of the reddit.com/r/dailyprogrammer challenge #294
# see here: https://www.reddit.com/r/dailyprogrammer/comments/5go843/20161205_challenge_294_easy_rack_management_1/
import timeit

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
                cError = cError + (dicword[z] - letters[z])
                devalue += ltrVal[z] * (dicword[z] - letters[z])

        else:
            cError += dicword[z]
            devalue += ltrVal[z] * dicword[z]

    return {'distance':cError, 'devalue':devalue}


def findbestword(letters, userword):
    bestscore = 0
    bestwords = {}
    f = open('enable1.txt', 'r')
    for line in f:
        xline = line.lower().strip("\r\n")
        linedict = countletters(xline)
        compx = wordcompare(letters, linedict)
        if compx['distance'] - letters['?'] <= 0 and countwordval(xline) - compx['devalue'] >= bestscore:
            bestscore = countwordval(xline)
            bestwords[xline] = countwordval(xline)

    f.close()

    #pick top word(s) with available given letters
    betterword = {}
    for words in bestwords:
        if countwordval(words) >= bestscore:
            betterword[words] = countwordval(words)

    return betterword

def main():
    print "\n**Scrabble Finder v1.0\n" \
          "**Enter the letters you have and the word you want to play.\n" \
          "**This will tell you if you can play the word or not.\n" \
          "**Use a ? (question mark) for wildcard/blank tiles.\n"

    uLetters = raw_input("What letters do you have:>")

    uWord = raw_input("What word do you want to create?>")

    # count up letters in the letter list - using our shiny new function 'countletters'.
    wDict = countletters(uLetters.lower())
    xDict = countletters(uWord.lower())

    # lastly, compare the number of letters in the desired word to the count of the letter list
    # cError is the number of letters not matching; if the number of wildcards is equal or exceeds that number,
    #  the word is valid to be played
    comp = wordcompare(wDict,xDict)

    wildcards = comp['distance'] - wDict['?']
    best = findbestword(wDict, uWord)


    # let the user know the good or bad news
    if wildcards <= 0:
        print "\nYou can play that word! Point Value: " + str(countwordval(uWord) - comp['devalue'])
        print "Given your letters, an even better word would be: " + str(best)
    else:
        print "\nSorry, that word is not possible with your current letters."
        print "Number of wildcards available: " + str(wDict['?'])
        print "Number of additional wildcards needed: " + str(wildcards)
        print "The best word(s) you can play: " + str(best)

main()

print "\nExecuted in " + str(timeit.timeit())[:6] + " seconds\n"

