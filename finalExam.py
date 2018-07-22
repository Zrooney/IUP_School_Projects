rawList = []
mySubList = []
myList = []
mySubListRaw = []
avgGrade = 0
gradeCount = 0
nameSelect = 0
x = 0
i = 0
count = 0

#stores txt file in big ass list, makes every character lower case and gets rid of the new line
rawList.append(open('Scores.txt').read().lower().split('\n'))

#flattens the list to get more than 1 element in the list
for sublist in rawList:
    for item in sublist:
        myList.append(item)

#pops the '' index at the end of the list
myList.pop()

#converts the list into a raw string into a master list called myList. All the data values
#are split at the comma
myString = ",".join([str(x) for x in myList])
myList = myString.split(',')

#creates seperate sub lists for each student
for i in range(0, len(myString), 6):
    mySubListRaw.append(myList[i:i+6])

#gets rid of the blank lists at the end of the mySubListRaw
for y in mySubListRaw:
    if y != []:
        mySubList.append((y))

#lets the user select either first or last name
nameSelect = input('Enter 1 for last name search, 2 for first name search \n')
if nameSelect == '1':
    studentName = input("enter students last name \n")
    studentName = studentName.strip().lower()
    for x in range(0,len(myList), 6):
        #does the math to calculate the averages on the fly
        if studentName in myList[x]:
            gradeCount = x + 2
            for gradeCount in range(gradeCount, gradeCount + 4):
                avgGrade += float(myList[gradeCount])
                count += 1
            avgGrade = avgGrade / count
            print(mySubList[x // 6], "Avg grade is", avgGrade, '\n')
            avgGrade = 0
            count = 0
elif nameSelect == '2':
    studentName = input("enter students first name \n")
    studentName = studentName.strip().lower()
    for x in range(1,len(myList), 6):
        if studentName in myList[x]:
            gradeCount = x + 1
            for gradeCount in range(gradeCount, gradeCount + 4):
                avgGrade += float(myList[gradeCount])
                count += 1
            avgGrade = avgGrade / count
            print(mySubList[x // 6], "Avg grade is", avgGrade, '\n')
            avgGrade = 0
            count = 0
else:
    print('Name not found in database')




