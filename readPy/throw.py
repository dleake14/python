import random, time, string

limit = 20
message= {}

def get_randChar():
    randRet = random.choice(string.ascii_letters)
    return randRet


for x in range(limit):
    if x == 5:
        for g in range(limit):
            message[x,g] = ("David".center(limit,"*"))[g]
    if x == 10:
        for g in range(limit):
            message[x,g] = ("Loves".center(limit,"*"))[g]
    if x == 15:
        for g in range(limit):
            message[x,g] = ("Laurel".center(limit,"*"))[g]
    if x % 5 != 0 or x == 0: 
        for g in range(limit):
            message[x,g] = get_randChar()

arOut= ['f'] * limit
for m in range (limit):
    for p in range (limit):
        arOut[p] = message[m,p]
        if m % 5 != 0 or x == 0: 
            print(arOut[p], end="")
            time.sleep(.01)
        if m % 5 == 0 and m != 0:
            print(arOut[p], end="")
            time.sleep(.1)
    print(end="\r")

