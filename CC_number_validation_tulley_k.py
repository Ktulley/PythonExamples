#Korey Tulley
#388555
#Homework 3 Program Set 2
#use descriptive comments
#use descriptive names for variables
#all monetary values 2 decimal places
#

def main():
    '''Reads credit card numbers the specified amount of times and calls other functions'''
    runs = int(input("How many credit card numbers do you want to check? "))
    for num in range(0, (runs)):
        number = input("Enter a credit card number: ")
        validity = isValid(number)
        if validity is True:
            print(number + " is valid")
        elif validity is False:
            print(number + " is invalid")
        else:
            print("Error, isValid() didn't return T/F")
        print()

    
def isValid(cardNumber : str)->(bool):
    '''takes card number and runs it through functions to test validity'''
    if len(cardNumber) >= 13 and len(cardNumber) <= 16:
    #I wasn't 100% sure we learned len, but seeing as we're using startswith I think its fair, if not you'd have to
    #write a for loop to count the variable
        if cardNumber.startswith("4") or cardNumber.startswith("5") or cardNumber.startswith("6") or cardNumber.startswith("37"):
            eSum = sumOfDoubleEvenPlace(cardNumber)
            oSum = sumOfOddPlace(cardNumber)
            tSum = oSum + eSum
            if (tSum % 10) == 0:
                ##print(tSum, oSum, eSum)
                return True
            else:
                ##print("failed sum functions")
                ##print(tSum, oSum, eSum)
                return False
        else:
            ##print("failed starts with")
            return False
    else:
        ##print("failed card length")
        return False
    
    
def sumOfDoubleEvenPlace(cardNumber : str)->(int):
    '''doubles every second digit from right to left, and if double digit result adds them together to get a single digit'''
    eSum = 0
    for i in range(len(cardNumber)-2, -1, -2):
        ##print(int(cardNumber[i]))
        digit = getDigit((int(cardNumber[i]) * 2))
        ##print(digit)
        eSum = digit + eSum
    return eSum
    
def getDigit(number : int)->(int):
    '''checks if 1 or 2 digits, if 2, splits and adds the numbers'''
    if (number < 10):
        ##print("one digit")
        return number
    else:
        ##print(number)
        ##print("two digits")
        lastDigit = int(number % 10)
        firstDigit = int(number / 10)
        newNumber = lastDigit + firstDigit      
        return newNumber
    
def sumOfOddPlace(cardNumber : str)->(int):
    oSum = 0
    for i in range(len(cardNumber)-1, -1, -2):
        digit = int(cardNumber[i])
        oSum = digit + oSum
    return oSum

if __name__ == "__main__":
    main()
    

#ask user to stop the program
input('\n\nPress the enter key to quit')

##Output
##Test Run 1
##How many credit card numbers do you want to check? 2
##Enter a credit card number: 4388576018402626
##4388576018402626 is invalid
##
##Enter a credit card number: 4388576018410707
##4388576018410707 is valid
##
##
##
##Press the enter key to quit


##Output
##Test Run 2
##How many credit card numbers do you want to check? 0
##
##
##Press the enter key to quit


##Output
##Test Run 3
##How many credit card numbers do you want to check? 3
##Enter a credit card number: 12345678
##12345678 is invalid
##
##Enter a credit card number: 5169769005222217
##5169769005222217 is valid
##
##Enter a credit card number: 6011655276746808
##6011655276746808 is invalid
##
##
##
##Press the enter key to quit


##Output
##Test Run 4
##How many credit card numbers do you want to check? 4
##Enter a credit card number: 6123456789123
##6123456789123 is invalid
##
##Enter a credit card number: 6178937299403
##6178937299403 is invalid
##
##Enter a credit card number: 6178937299430
##6178937299430 is valid
##
##Enter a credit card number: 5178937299431
##5178937299431 is invalid
##
##
##
##Press the enter key to quit



##Output
##Test Run 5
##How many credit card numbers do you want to check? 6
##Enter a credit card number: 37227521093827
##37227521093827 is invalid
##
##Enter a credit card number: 37227521093828
##37227521093828 is invalid
##
##Enter a credit card number: 37227521093829
##37227521093829 is valid
##
##Enter a credit card number: 37227521093820
##37227521093820 is invalid
##
##Enter a credit card number: 5169769005222316
##5169769005222316 is valid
##
##Enter a credit card number: 5169769005222415
##5169769005222415 is valid
##
##
##
##Press the enter key to quit
