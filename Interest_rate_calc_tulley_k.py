#Korey Tulley
#388555
#Homework # Program Set #
#use descriptive comments
#use descriptive names for variables
#all monetary values 2 decimal places

class Loan:
    # Creating a class to create objects that are instances of loans
    
    def __init__(self, rate = 2.5, years = 1, amount = 1000, name = ""):
        '''initializing the loan'''
        self.__rate = rate
        self.__years = years
        self.__amount = amount
        self.__name = name


    def getRate(self):
        '''Returns the rate '''
        return self.__rate

        
    def getYears(self):
        '''Returns the years '''
        return self.__years

  
    def getAmount(self):
        '''Returns the amount '''
        return self.__amount

  
    def getName(self):
        '''Returns the name '''
        return self.__name

  
    def setRate(self, rate):
        '''Changes the rate '''
        self.__rate = rate

  
    def setYears(self, years):
        '''Changes the years '''
        self.__years = years


    def setAmount(self, amount):
        '''Changes the amount'''
        self.__amount = amount


    def setName(self, name):
        '''Changes the name '''
        self.__name = name


    def getMonthlyPayment(self)->float:
        '''Returns the monthly payment for the specified loan'''
        monthlyInterestRate = self.__rate /  1200
        monthlyPayment = self.__amount * monthlyInterestRate / (1 - (1 / (1 + monthlyInterestRate) ** (self.__years * 12)))
        return monthlyPayment

        
    def getTotalPayment(self)->float:
        '''Returns the total amount to be paid for the specified loan'''
        totalPayment = self.getMonthlyPayment() * self.__years * 12
        return totalPayment


def main():
    '''creates an object for the loan, asks the user to set the data fields
    
    '''
    #create an instance of the loan
    loan1 = Loan()

    #have the user input the data fields
    loan1.setRate(float(input("Enter yearly interest rate: ")))
    loan1.setYears(float(input("Enter number of years as an integer: ")))
    loan1.setAmount(float(input("Enter loan amount: ")))
    loan1.setName(input("Enter a borrowers name: "))

    #return the information to the user and call the calcs
    print("The loan is for ", loan1.getName())
    print("The monthly payment is ", format(loan1.getMonthlyPayment(), ',.2f'))
    print("The total payment is ", format(loan1.getTotalPayment(), ',.2f'))
    
    #junk I used for debug
##    print("The is debug rate", loan1.getRate())
##    print("The is debug years", loan1.getYears())
##    print("The is debug amount", loan1.getAmount())
##    print("The is debug name", loan1.getName())
    
    #create a variable for the while loop
    changeAmount = "Y"
    
    #continue while loop aslong as it isn't an empty string
    while (changeAmount != ""):
        changeAmount = input("\nDo you want to change the loan amount? Y for yes or enter to quit ")
        #if the user wants edit the object and rerun the clacs
        if (changeAmount == "Y" or changeAmount == "y"):
            loan1.setAmount(float(input("Enter new loan amount ")))
            print("The loan is for ", loan1.getName())
            print("The monthly payment is ", format(loan1.getMonthlyPayment(), ',.2f'))
            print("The total payment is ", format(loan1.getTotalPayment(), ',.2f'))

    
if __name__ == "__main__":
    main()
    


##Output
##Test Run 1
##Enter yearly interest rate: 2.5
##Enter number of years as an integer: 5
##Enter loan amount: 1000.00
##Enter a borrowers name: John Jones
##The loan is for  John Jones
##The monthly payment is  17.75
##The total payment is  1,064.84
##
##Do you want to change the loan amount? Y for yes or enter to quit y
##Enter new loan amount 5000
##The loan is for  John Jones
##The monthly payment is  88.74
##The total payment is  5,324.21
##
##Do you want to change the loan amount? Y for yes or enter to quit


##Output
##Test Run 2
##Enter yearly interest rate: 4.5
##Enter number of years as an integer: 10
##Enter loan amount: 10000.00
##Enter a borrowers name: Big Numbers
##The loan is for  Big Numbers
##The monthly payment is  103.64
##The total payment is  12,436.61
##
##Do you want to change the loan amount? Y for yes or enter to quit y
##Enter new loan amount 100000000
##The loan is for  Big Numbers
##The monthly payment is  1,036,384.09
##The total payment is  124,366,090.51
##
##Do you want to change the loan amount? Y for yes or enter to quit

    
##Output
##Test Run 3
##Enter yearly interest rate: 0.5
##Enter number of years as an integer: 1
##Enter loan amount: 5
##Enter a borrowers name: Small Numbers
##The loan is for  Small Numbers
##The monthly payment is  0.42
##The total payment is  5.01
##
##Do you want to change the loan amount? Y for yes or enter to quit 

##Output
##Test Run 4
##Enter yearly interest rate: 3.256
##Enter number of years as an integer: 10.4
##Enter loan amount: 6123461.42
##Enter a borrowers name: Weird Numbers
##The loan is for  Weird Numbers
##The monthly payment is  57,907.56
##The total payment is  7,226,863.20
##
##Do you want to change the loan amount? Y for yes or enter to quit 

##Output
##Test Run 5
##Enter yearly interest rate: 120
##Enter number of years as an integer: .5
##Enter loan amount: 0
##Enter a borrowers name: Broken Numbers
##The loan is for  Broken Numbers
##The monthly payment is  0.00
##The total payment is  0.00
##
##Do you want to change the loan amount? Y for yes or enter to quit y
##Enter new loan amount .5
##The loan is for  Broken Numbers
##The monthly payment is  0.11
##The total payment is  0.69
##
##Do you want to change the loan amount? Y for yes or enter to quit 
