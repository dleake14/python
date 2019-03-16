import datetime
lookfor = "#FILE READ#"
found = ''
file = open("Input.txt","r")
for line in file:
    if lookfor not in line:
        current = datetime.datetime.now()
        file.close()
        file = open("Input.txt","a")
        file.write("\n#FILE READ# ")
        file.write(str(current))
        print("Wasn't timestamped, so we're timestamping it")
        file.close()
        break
    else:
        print("Already in there, bro")
        file.open("Input.txt","r")
        print(file.read())



# file = open("Input.txt","r+")
# print(file.read())
print('--------')




