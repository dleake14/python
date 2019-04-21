# Dictionaries (Dict) are data sructures that map objects in key\value pairs
rpsDict = {
    "rock": 1,
    "paper": 2,
    "scissors": 3,
}

# Declare functions above the 'main' code
# Function that gets the input handed to it by 'main' code and tests
def rpsInput (rps):
    try: 
        return rpsDict[rps]
    except:
        return "error"

# 'Main" Code
print("Yo, you wanna play that RPS, dawg?")
yourMom = input("PLAYER 1:\nPlease enter 'rock', 'paper' or 'scissors'\n")
play1 = rpsInput(yourMom)
if play1 == "error":
    print ("They hell, brah?")
else:
    yourMom2 = input("PLAYER 2:\nPlease enter 'rock', 'paper' or 'scissors'\n")
    play2 = rpsInput(yourMom2)
if play2 == "error":
    print ("They hell, brah?")
else:
    if play1 == play2:
        print ("tie")
    else: 
        if play1 == (play2 + 1) or play1 == (play2 - 2):
            print ("Player 1 Wins because " + yourMom + " beats " + yourMom2)
        else:
            print ("Player 2 Wins because " + yourMom2 + " beats " + yourMom)
        