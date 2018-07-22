myList = [1011, 1111, 111, 0b10111]
binaryNum = 0
decimalNum = 0
for i in myList:
    binaryNum = i
    decimalNum = 0
    currentPower = 0
    while binaryNum != 0:
        decimalNum += (binaryNum % 10) * (2 ** currentPower)
        currentPower += 1
        binaryNum = binaryNum/10
    print(decimalNum)