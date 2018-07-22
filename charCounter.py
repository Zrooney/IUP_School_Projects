charCount = 0
charAscii = 0
listChar = []
asciiVowels = {65, 69, 73, 79, 85, 97, 101, 105, 111, 117}

userInput = input("Enter a string")
for letter in userInput:
    listChar.append(letter)

for charAscii in asciiVowels:
    for i in userInput:
        if (ord(i)) == charAscii:
            charAscii += charAscii
            print(i, "count is", listChar.count(i))

#the following code works, but prints the out however many characters there are in string
#for char in listChar: #define range of alphabet in ascii here
    #for i in range(65 , 90) and range(97,122):
 #   charCount = listChar.count(char)
#   if (charCount > 0):
#           print(char,"count is",charCount)



