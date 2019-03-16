import time, sys

home = "home = "
away = "away = "
qtr = "qtr = "
ascore = "ascore = "
hscore = "hscore = "
uhscore = ""
uacscore = ""
uqtr = ""


writer = open("sbdat.txt", "r").read()


def datPrint(var):
    print(writer[writer.find(var) + len(var):-(len(writer) - writer.find(";", writer.find(var)))].center(10), end="")
    return ""


def fullPrint():
    print("*****************************")
    print(datPrint(away), end="")
    print("QTR".center(10), end="")
    print(datPrint(home))
    print(datPrint(ascore), end="")
    print(datPrint(qtr), end="")
    print(datPrint(hscore))
    print("*****************************")

fullPrint()
for x in range(30):
    fullPrint()
    time.sleep(1)
# print("\END OF PART ONE/")
#
# def datWrite(var, nVar):
#
#
#     #inn = open("sbdat.txt").read()
#     #out = open("sbdat.txt","w")
#     rep = ''
#     rep = writer[writer.find(var) + len(var):-(len(writer) - writer.find(";", writer.find(var)))]
#     rep = rep.replace(rep, nVar)
#     return ""
#
# uhscore = input("Enter new Home Score\n")
# datWrite(hscore, uhscore)

