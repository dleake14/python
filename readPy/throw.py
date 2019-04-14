import random, time, string

limit = 20
x = 0
message= {}

def get_randString():
    randRet = ['Q'] * limit
    for f in range(limit):
        randRet[f] = random.choice(string.ascii_letters)
    return randRet


for x in range(limit):
    if x == 5:
        message[x] = ("David".center(limit,"*"))
    if x == 10:
        message[x] = ("Loves".center(limit,"*"))
    if x == 15:
        message[x] = ("Laurel".center(limit,"*"))

arOut= ['f'] * limit
for p in range (limit):
    arOut = message[p]
    print(arOut[p], end="")
    time.sleep(.25)
    print(end="\r")

