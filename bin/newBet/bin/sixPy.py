import time, sys, subprocess, curses


home = "home = "
away = "away = "
qtr = "qtr = "
ascore = "ascore = "
hscore = "hscore = "
uhscore = ""
uacscore = ""
uqtr = ""




def datPrint(var):
    file = open("sbdat.txt", "r")
    writer = file.read()
    print(writer[writer.find(var) + len(var):-(len(writer) - writer.find(";", writer.find(var)))].center(10), end="")
    file.close()
    return ""


def fullPrint():
    print("\n\n\n\n\n")
    print("*****************************")
    print(datPrint(away), end="")
    print("QTR".center(10), end="")
    print(datPrint(home), end="\n")
    print(datPrint(ascore), end="")
    print(datPrint(qtr), end="")
    print(datPrint(hscore), end="\n")
    print("*****************************")



#fullPrint()
for x in range(50):
    fullPrint()
    #time.sleep(1)


print("\END OF PART ONE/")


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

