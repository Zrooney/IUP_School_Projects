import random
totalWinnings = 0
for i in range(10):
    userInput = int(input("enter num between 0 and 999"))
    computerRoll = random.randint(0,999)
    if computerRoll == userInput:
        print("You won $20")
        totalWinnings = totalWinnings + 20
    elif (computerRoll%100) == (userInput%100):
        print("You won $10")
        totalWinnings = totalWinnings + 10
    elif (computerRoll%10) == (userInput%10):
        print("You won $5")
        totalWinnings = totalWinnings + 5
    else:
        print("you won nothing!")
        totalWinnings = totalWinnings - 5
    #print(computerRoll)
    #print(totalWinnings)
    i += 1

if totalWinnings >= 0:
    print("Total money won", totalWinnings)
else:
    print("Total money lost", totalWinnings)
#print(userInput)