def isPrime(number):
    if number == 1:
        return True
    elif number == 2:
        return True
    elif number % 2 == 0:
        return False
    else:
        for counter in range (2, number // 2 + 1):
            if number % counter == 0:
                print("{0} is not prime".format(number))
                return False
            return True

def divisor(number):
    myList = []
    for i in range(1, number //2 + 1):
        if number % i == 0:
            myList.append(i)
        return myList


numberString = input(("Please enter a number"))
if numberString.isdigit():
    number = int(numberString)
    if isPrime(number):
        print("{} is prime".format(number))
    else:
        print("{} is not prime".format(number))
        print("The divisors are {0}".format(divisor(number)))
else:
    print("No valid number entered")