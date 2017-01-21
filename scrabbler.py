# coding: UTF-8
# Scrabbler by KNOVA
# submitted as part of the reddit.com/r/dailyprogrammer challenge #294
# see here: https://www.reddit.com/r/dailyprogrammer/comments/5go843/20161205_challenge_294_easy_rack_management_1/

print "\n**Scrabble Finder v1.0\n" \
      "**Enter the letters you have and the word you want to play.\n" \
      "**This will tell you if you can play the word or not.\n" \
      "**Use a ? (question mark) for wildcard/blank tiles.\n"


uLetters = raw_input("What letters do you have:>")

uWord = raw_input("What word do you want to create?>")

wDict = {} #for tracking letters in the user's letter list
xDict = {} #for tracking letters in the user's desired word

#count up letters in the letter list.
for c in uLetters:
    if c in wDict:
        wDict[c] = wDict[c] + 1
    else:
        wDict[c] = 1

#count all the letters in the desired word
for x in uWord:
    if x in xDict:
        xDict[x] = xDict[x] + 1
    else:
        xDict[x] = 1

#lastly, compare the number of letters in the desired word to the count of the letter list
cError = 0
for z in uWord:
    if z in wDict:
        if wDict[z] >= xDict[z]:
            cError = 0
        else:
            cError = 1
            break
    else:
        cError = 1
        break

#let the user know the good or bad news
if cError == 0:
    print "You can play that word!"
else:
    print "Sorry, that word not possible with your current letters."