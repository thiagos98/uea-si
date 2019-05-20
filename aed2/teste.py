
import sys
#sys.path.append('C:\\Python27\\CherryPy-3.2.2')
import cherrypy
import random
import string

CONST_STR = "SEMP TCL INDUSTRIA E COMERCIO ELETROELETRONICO"
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

def modRandStr(randStr):    # modify each character of randStr with probability CONST_PROB%
    """Return modified randStr -- each character of randStr is modified with probability CONST_PROB%."""
    newRandStr = randStr
    for x in range(0, len(CONST_STR)):
        randInt = random.randint(1, 100)
        if randInt <= CONST_PROB:
            newRandStr = newRandStr[:x] + genRandChar() + newRandStr[x + 1:]
    return newRandStr

print(modRandStr(genRandStr()))
