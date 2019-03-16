home = "home = "
away = "away = "
qtr = "qtr = "
ascore = "ascore = "
hscore = "hscore = "

lines = open("sbdat.txt", "r").read()


def datPrint(str):
    print(lines[lines.find(str) + len(str):-(len(lines) - lines.find(";", lines.find(str)))], end="")


datPrint(home)
datPrint(away)
datPrint(hscore)
datPrint(ascore)
datPrint(qtr)

print("\n\n\END/")
