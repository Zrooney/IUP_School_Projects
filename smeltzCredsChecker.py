userName = input("Enter user name")
userPass = input("Enter Password, multiple passwords seperated with comma")
#specialChar = {'$', '#', '@'}
specialChar = "$#@"
lowerCase = "abcdefghijklmnopqrstuvwxyz"
upperCase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numberList = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
isLowerCase = False
isUpperCase = False
isNumberList = False
isSpecialChar = False
char = ""

if 6 <= len(userPass) <= 12:
    for char in userPass:
        if char in lowerCase:
            isLowerCase = True
        if char in upperCase:
            isUpperCase = True
        if char in numberList:
            isNumberList = True
        if char in specialChar:
            isSpecialChar =  True
else:
    print("Not right length")

if isLowerCase == True and isUpperCase == True and isNumberList == True and isSpecialChar == True:
            print("valid pass")
else:
    print("no valid pass")