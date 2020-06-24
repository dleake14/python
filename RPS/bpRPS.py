import random
computer = random.randint(1, 4)
a = 5
while a > 2:
    users = input("How many users? (1 or 2): ")
    if users == "1":
        a = 1
    elif users == "2":
        a = 2
    elif users == "quit":
        break
    else:
        print("Please enter a valid number of players or type 'quit'")
while a == 1:
    user1 = input("Choose either rock, paper, or scissors?: ")
    computer = random.randint(1, 4)
    if user1 == "rock":
        user1 = 1
    if user1 == computer:
        print("You tied, try again")
    elif user1 == (computer - 1):
        print("The computer won! Try again!")
    else:
        print("Congrats! You won!")
    playagain = input("Do you want to play again? (y/n): ")
    if playagain == "n":
        print("Thanks for playing!")
        a = 5
    elif user1 == "paper":
        user1 = 2
    if user1 == computer:
        print("You tied, try again")
    elif user1 == (computer - 1):
        print("The computer won! Try again!")
    else:
        print("Congrats! You won!")
if playagain == "n":
    print("Thanks for playing!")
    a = 5
elif user1 == "scissors":
    user1 = 3
if user1 == computer:
    print("You tied, try again")
elif user1 == (computer + 2):
    print("The computer won! Try again!")
else:
    print("Congrats! You won!")
if playagain == "n":
    print("Thanks for playing!")
    a = 5
else:
    print("Please choose either rock, paper, or scissors.")

while a == 2:
    user1name = input("What is player 1's name?: ")
    user2name = input("What is player 2's name?: ")
while user1name != "":
    user1 = ""
    user2 = ""
    options = ["rock", "paper", "scissors"]
while user1 not in options:
    user1 = input(user1name + ", choose either rock, paper, or scissors?: ")
    if user1 not in options:
        print(user1name + ", please choose either rock, paper, or scissors: ")
while user2 not in options:
    user2 = input(user2name + ", choose either rock, paper, or scissors?: ")
    if user2 not in options:
        print(user2name + ", please choose either rock, paper, or scissors: ")
        if user1 == user2:
            print("You TIED! Would your like to play again? (y/n)")
            playagain = input()
        elif user1 == "rock":
            if user2 == "paper":
                print(user2name + " WINS! Would you like to play again? (y/n)")
                playagain = input()
            else:
                print(user1name + " WINS! Would you like to play again? (y/n)")
                playagain = input()
            # elif user1 == "paper":
            if user2 == "rock":
                print(user1name + " WINS! Would you like to play again? (y/n)")
                playagain = input()
            else:
                print(user2name + " WINS! Would you like to play again? (y/n)")
                playagain = input()
            if user2 == "rock":
                print(user2name + " WINS! Would you like to play again? (y/n)")
                playagain = input()
            else:
                print(user1name + " WINS! Would you like to play again? (y/n)")
                playagain = input()
            if playagain == "n":
                print("Thanks for playing!")
                a = 5
    break
