import time, sys, subprocess, curses


home = "home = "
away = "away = "
qtr = "qtr = "
ascore = "ascore = "
hscore = "hscore = "
uhscore = ""
uacscore = ""
uqtr = ""

stdscr.clear()
stdscr.refresh()

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




for x in range(3):
    fullPrint()
    time.sleep(5)


print("\END OF PART PROGRAM/")

