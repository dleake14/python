
lines = open("sbdat.txt", "r").read()

print(lines[lines.find("home = ")+len("home = "):-(len(lines)-lines.find(";", lines.find("home =")))])
print(lines[lines.find("away = ")+len("away = "):-(len(lines)-lines.find(";", lines.find("away =")))])
print(lines[lines.find("hscore = ")+len("hscore = "):-(len(lines)-lines.find(";", lines.find("hscore =")))])
print(lines[lines.find("ascore = ")+len("ascore = "):-(len(lines)-lines.find(";", lines.find("ascore =")))])
print(lines[lines.find("qtr = ")+len("qtr = "):-(len(lines)-lines.find(";", lines.find("qtr =")))])


print("\END/")
