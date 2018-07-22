numbers = input("Enter num, seprated by commas: \n")
print(numbers)
totalNumber = 0
ind = 0
listNumber = []
for number in numbers:
    if number.isdigit():
        totalNumber += int(number)
        listNumber.append(number)
print(listNumber)
print("Total amount", totalNumber)

print(max(listNumber))
print(min(listNumber))




# numberList = numbers.split(",")
# sum = 0
# for num in numberList:
#     print(num.lstrip())
#     sum += int(num.strip())
# print(sum)
