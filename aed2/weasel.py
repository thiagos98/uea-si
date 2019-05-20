import sys
#sys.path.append('C:\\Python27\\CherryPy-3.2.2')
import cherrypy
import random
import string

CONST_STR = "THIAGO SANTOS BORGES"
CONST_SIZE = 100
CONST_PROB = 5


def genRandChar():  # print random uppercase letter or whitespace
    """Return random uppercase letter or whitespace."""
    return random.choice(string.ascii_uppercase + string.whitespace)


def genRandStr():   # print random string of length CONST_STR
    """Return random string of length CONST_STR."""
    randStr = ''
    for x in range(0, len(CONST_STR)):
        randStr = randStr + genRandChar()
    return randStr


def compStr(randStr):   # compare CONST_STR with randStr
    """Return index of randStr -- number of common characters in randStr and CONST_STR."""
    randStrIndex = 0
    for i in range(0, len(CONST_STR)):
        if CONST_STR[i] == randStr[i]:
            randStrIndex += 1
    return randStrIndex


def modRandStr(randStr):    # modify each character of randStr with probability CONST_PROB%
    """Return modified randStr -- each character of randStr is modified with probability CONST_PROB%."""
    newRandStr = randStr
    for x in range(0, len(CONST_STR)):
        randInt = random.randint(1, 100)
        if randInt <= CONST_PROB:
            newRandStr = newRandStr[:x] + genRandChar() + newRandStr[x + 1:]
    return newRandStr


class WeaselProgram:
    def index(self):
        loopNumber = 0
        strFound = False
        randStr = genRandStr()
        resultList = []
        while not strFound:
            strList = [''] * CONST_SIZE
            indexList = [None] * CONST_SIZE
            for x in range(0, CONST_SIZE):
                strList[x] = modRandStr(randStr)
                indexList[x] = compStr(strList[x])
            maxIndex = max(indexList)
            if maxIndex == len(CONST_STR):
                strFound = True
            randStr = strList[indexList.index(maxIndex)]
            resultList.append(str(loopNumber) + ": " + randStr + " -- score: " + str(maxIndex))
            loopNumber += 1
        return '<br>'.join(resultList)
    index.exposed = True

cherrypy.quickstart(WeaselProgram())
