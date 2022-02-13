#Korey Tulley
#388555
#Homework 2 Program Set 1
#use descriptive comments
#use descriptive names for variables
#all monetary values 2 decimal places

#Data/input
income = int(input("Enter income as an integer with no commas: "))

#begin while loop
while income >= 0:
        
    #Calculating your 2017 tax
    if income <= 9325:
        tax2017 = 0.1 * income
    elif income <= 37950:
        tax2017 = (0.1 * 9325) + (0.15 * (income - 9325))
    elif income <= 91900:
        tax2017 = (0.1 * 9325) + (0.15 * (37950 - 9325)) + (0.25 * (income - 37950))
    elif income <= 191650:
        tax2017 = (0.1 * 9325) + (0.15 * (37950 - 9325)) + (0.25 * (91900 - 37950)) + (0.28 * (income - 91900))
    elif income <= 416700:
        tax2017 = (0.1 * 9325) + (0.15 * (37950 - 9325)) + (0.25 * (91900 - 37950)) + (0.28 * (191650 - 91900)) + (0.33 * (income - 191650))
    elif income <= 418400:
        tax2017 = (0.1 * 9325) + (0.15 * (37950 - 9325)) + (0.25 * (91900 - 37950)) + (0.28 * (191650 - 91900)) + (0.33 * (416700 - 191650)) + (0.35 * (income - 416700))
    else:
        tax2017 = (0.1 * 9325) + (0.15 * (37950 - 9325)) + (0.25 * (91900 - 37950)) + (0.28 * (191650 - 91900)) + (0.33 * (416700 - 191650)) + (0.35 * (418400 - 416700)) + (0.396 * (income - 418400))
        
    #Calculating your 2018 tax
    if income <= 9525:
        tax2018 = 0.1 * income
    elif income <= 38700:
        tax2018 = (0.1 * 9525) + (0.12 * (income - 9525))
    elif income <= 82500:
        tax2018 = (0.1 * 9525) + (0.12 * (38700 - 9525)) + (0.22 * (income - 38700))
    elif income <= 157500:
        tax2018 = (0.1 * 9525) + (0.12 * (38700 - 9525)) + (0.22 * (82500 - 38700)) + (0.24 * (income - 82500))
    elif income <= 200000:
        tax2018 = (0.1 * 9525) + (0.12 * (38700 - 9525)) + (0.22 * (82500 - 38700)) + (0.24 * (157500 - 82500)) + (0.32 * (income - 157500))
    elif income <= 500000:
        tax2018 = (0.1 * 9525) + (0.12 * (38700 - 9525)) + (0.22 * (82500 - 38700)) + (0.24 * (157500 - 82500)) + (0.32 * (200000 - 157500)) + (0.35 * (income - 200000))
    else:
        tax2018 = (0.1 * 9525) + (0.12 * (38700 - 9525)) + (0.22 * (82500 - 38700)) + (0.24 * (157500 - 82500)) + (0.32 * (200000 - 157500)) + (0.35 * (500000 - 200000)) + (0.37 * (income - 500000))

    #The difference between the 2018 & 2017
    #and difference as a % of 2017 taxes
    diff = float(tax2018-tax2017)
    if tax2017 != 0:
        diffPercent = float((abs(diff / tax2017))*100)
    else:
        diffPercent = 0
    
    #printing the results
    print("Income:", income)
    print("2017 tax:", format(tax2017, '.2f'))
    print("2018 tax:", format(tax2018, '.2f'))
    print("Difference:", format(diff, '.2f'))
    print("Difference (precent):", format(diffPercent, '.2f'))
    print()
    income = int(input("Enter income as an integer with no commas: "))
    
#ask user to stop the program
input('\n\nPress the enter key to quit')

##Output
##Test Run 1
##Enter income as an integer with no commas: 8000
##Income: 8000
##2017 tax: 800.00
##2018 tax: 800.00
##Difference: 0.00
##Difference (precent): 0.00
##
##Enter income as an integer with no commas: 15000
##Income: 15000
##2017 tax: 1783.75
##2018 tax: 1609.50
##Difference: -174.25
##Difference (precent): 9.77
##
##Enter income as an integer with no commas: 40000
##Income: 40000
##2017 tax: 5738.75
##2018 tax: 4739.50
##Difference: -999.25
##Difference (precent): 17.41
##
##Enter income as an integer with no commas: 100000
##Income: 100000
##2017 tax: 20981.75
##2018 tax: 18289.50
##Difference: -2692.25
##Difference (precent): 12.83
##
##Enter income as an integer with no commas: 200000
##Income: 200000
##2017 tax: 49399.25
##2018 tax: 45689.50
##Difference: -3709.75
##Difference (precent): 7.51
##
##Enter income as an integer with no commas: 500000
##Income: 500000
##2017 tax: 153818.85
##2018 tax: 150689.50
##Difference: -3129.35
##Difference (precent): 2.03
##
##Enter income as an integer with no commas: 1000000
##Income: 1000000
##2017 tax: 351818.85
##2018 tax: 335689.50
##Difference: -16129.35
##Difference (precent): 4.58
##
##Enter income as an integer with no commas: 10000000
##Income: 10000000
##2017 tax: 3915818.85
##2018 tax: 3665689.50
##Difference: -250129.35
##Difference (precent): 6.39
##
##Enter income as an integer with no commas: -1
##
##
##Press the enter key to quit

##Output
##Test Run 2
##Enter income as an integer with no commas: -1
##
##
##Press the enter key to quit

##Output
##Test Run 3
##Enter income as an integer with no commas: 38000
##Income: 38000
##2017 tax: 5238.75
##2018 tax: 4369.50
##Difference: -869.25
##Difference (precent): 16.59
##
##Enter income as an integer with no commas: 416800
##Income: 416800
##2017 tax: 120945.25
##2018 tax: 121569.50
##Difference: 624.25
##Difference (precent): 0.52
##
##Enter income as an integer with no commas: 90
##Income: 90
##2017 tax: 9.00
##2018 tax: 9.00
##Difference: 0.00
##Difference (precent): 0.00
##
##Enter income as an integer with no commas: 90000
##Income: 90000
##2017 tax: 18238.75
##2018 tax: 15889.50
##Difference: -2349.25
##Difference (precent): 12.88
##
##Enter income as an integer with no commas: -100000000000
##
##
##Press the enter key to quit

##Output
##Test Run 4
##Enter income as an integer with no commas: 0
##Income: 0
##2017 tax: 0.00
##2018 tax: 0.00
##Difference: 0.00
##Difference (precent): 0.00
##
##Enter income as an integer with no commas: 100000000000
##Income: 100000000000
##2017 tax: 39599955818.85
##2018 tax: 36999965689.50
##Difference: -2599990129.35
##Difference (precent): 6.57
##
##Enter income as an integer with no commas: 1
##Income: 1
##2017 tax: 0.10
##2018 tax: 0.10
##Difference: 0.00
##Difference (precent): 0.00
##
##Enter income as an integer with no commas: 9524
##Income: 9524
##2017 tax: 962.35
##2018 tax: 952.40
##Difference: -9.95
##Difference (precent): 1.03
##
##Enter income as an integer with no commas: -1
##
##
##Press the enter key to quit

##Output
##Test Run 5
##Enter income as an integer with no commas: 5435325
##Income: 5435325
##2017 tax: 2108207.55
##2018 tax: 1976759.75
##Difference: -131447.80
##Difference (precent): 6.24
##
##Enter income as an integer with no commas: 435252
##Income: 435252
##2017 tax: 128178.64
##2018 tax: 128027.70
##Difference: -150.94
##Difference (precent): 0.12
##
##Enter income as an integer with no commas: 23523456
##Income: 23523456
##2017 tax: 9271107.43
##2018 tax: 8669368.22
##Difference: -601739.21
##Difference (precent): 6.49
##
##Enter income as an integer with no commas: 234324
##Income: 234324
##2017 tax: 60726.17
##2018 tax: 57702.90
##Difference: -3023.27
##Difference (precent): 4.98
##
##Enter income as an integer with no commas: -322345234
##
##
##Press the enter key to quit
