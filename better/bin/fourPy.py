home = "home = "
away = "away = "
qtr = "qtr = "
ascore = "ascore = "
hscore = "hscore = "

lines = open("sbdat.txt", "r").read()


def datPrint(str):
    print(lines[lines.find(str) + len(str):-(len(lines) - lines.find(";", lines.find(str)))].center(10), end="")
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

print("\END/")
