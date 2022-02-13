#Korey Tulley
#388555
#Homework 3 Program Set 1
#use descriptive comments
#use descriptive names for variables
#all monetary values 2 decimal places


#Data/input
def load()->(str, float, float, float, float):
    '''Gathers info for the stock exchange program'''
    name = input("Enter Stock name: ")
    amtShares = float(input("Enter Number of shares : "))
    pPrice = float(input("Enter Purchase price : "))
    sPrice = float(input("Enter selling price : "))
    commission = float(input("Enter Commission : "))
    return name, amtShares, pPrice, sPrice, commission


#Processing/Calculations
def joePaid(amtShares : float, pPrice : float)->(float):
    '''The amount of money Joe paid for the stock '''
    amtPaid = (amtShares * pPrice)
    return amtPaid


def joePCommission(commission : float, amtPaid : float)->(float):
    '''The amount of commission Joe paid his broker when he bought the stock. '''
    commissionP = (commission * amtPaid)
    return commissionP


def joeSold(amtShares : float, sPrice : float)->(float):
    '''The amount that Jim sold the stock for. '''
    amtSold = (amtShares *sPrice)
    return amtSold

def joeSCommission(commission : float, amtSold : float)->(float):
    '''The amount of commission Joe paid his broker when he sold the stock.'''
    commissionS = (commission * amtSold)
    return commissionS


def joeProfit(amtSold : float, commissionS : float, amtPaid : float, commissionP : float)->(float):
    '''The amount of money Joe had left when he sold the stock and paid his broker '''
    profit = ((amtSold - commissionS) - (amtPaid + commissionP))
    return profit

    
#output
def output(name : str, amtPaid : float, commissionP : float, amtSold : float, commissionS : float, profit : float) -> None:
    '''Prints the calculations for the stock exchange'''
    print("\n\nStock name : " + name)
    print("Amount paid for the stock:          $", format(amtPaid, '13,.2f'))
    print("Commission paid on the purchase:    $", format(commissionP, '13,.2f'))
    print("Amount the stock sold for:          $", format(amtSold, '13,.2f'))
    print("Commission paid on the sale:        $", format(commissionS, '13,.2f'))
    print("Profit (or loss if negative):       $", format(profit, '13,.2f'))


#main
def main():
    proceed = input("Enter your stock information? Type 'y' for yes, or 'n' for no: ")
    print()
    while proceed == "y":
        name, amtShares, pPrice, sPrice, commission = load()
        amtPaid = joePaid(amtShares, pPrice)
        commissionP = joePCommission(commission, amtPaid)
        amtSold = joeSold(amtShares, sPrice)
        commissionS = joeSCommission(commission, amtSold)
        profit = joeProfit(amtSold, commissionS, amtPaid, commissionP)
        output(name, amtPaid, commissionP, amtSold, commissionS, profit)
        print()
        proceed = input("\nEnter your stock information? Type 'y' for yes, or 'n' for no: ")
        print()
        

if __name__ == "__main__":
    main()

    
#ask user to stop the program
input('\n\nPress the enter key to quit')


##Output
##Test Run 1
##Enter your stock information? Type 'y' for yes, or 'n' for no: y
##
##Enter Stock name: Kaplac, Inc.
##Enter Number of shares : 10000
##Enter Purchase price : 33.92
##Enter selling price : 35.92
##Enter Commission : 0.04
##
##
##Stock name : Kaplac, Inc.
##Amount paid for the stock:          $    339,200.00
##Commission paid on the purchase:    $     13,568.00
##Amount the stock sold for:          $    359,200.00
##Commission paid on the sale:        $     14,368.00
##Profit (or loss if negative):       $     -7,936.00
##
##
##Enter your stock information? Type 'y' for yes, or 'n' for no: y
##
##Enter Stock name: IBM
##Enter Number of shares : 15000
##Enter Purchase price : 50.25
##Enter selling price : 100.20
##Enter Commission : 0.02
##
##
##Stock name : IBM
##Amount paid for the stock:          $    753,750.00
##Commission paid on the purchase:    $     15,075.00
##Amount the stock sold for:          $  1,503,000.00
##Commission paid on the sale:        $     30,060.00
##Profit (or loss if negative):       $    704,115.00
##
##
##Enter your stock information? Type 'y' for yes, or 'n' for no: n
##
##
##
##Press the enter key to quit


##Output
##Test Run 2
##
##Enter your stock information? Type 'y' for yes, or 'n' for no: n
##
##
##
##Press the enter key to quit


##Output
##Test Run 3
##Enter your stock information? Type 'y' for yes, or 'n' for no: y
##
##Enter Stock name: GME
##Enter Number of shares : 500
##Enter Purchase price : 4
##Enter selling price : 400
##Enter Commission : 0.02
##
##
##Stock name : GME
##Amount paid for the stock:          $      2,000.00
##Commission paid on the purchase:    $         40.00
##Amount the stock sold for:          $    200,000.00
##Commission paid on the sale:        $      4,000.00
##Profit (or loss if negative):       $    193,960.00
##
##
##Enter your stock information? Type 'y' for yes, or 'n' for no: n
##
##
##
##Press the enter key to quit


##Output
##Test Run 4
##Enter your stock information? Type 'y' for yes, or 'n' for no: y
##
##Enter Stock name: MSFT
##Enter Number of shares : 5000
##Enter Purchase price : 61.25
##Enter selling price : 59.90
##Enter Commission : 0.02
##
##
##Stock name : MSFT
##Amount paid for the stock:          $    306,250.00
##Commission paid on the purchase:    $      6,125.00
##Amount the stock sold for:          $    299,500.00
##Commission paid on the sale:        $      5,990.00
##Profit (or loss if negative):       $    -18,865.00
##
##
##Enter your stock information? Type 'y' for yes, or 'n' for no: y
##
##Enter Stock name: RAD
##Enter Number of shares : 2000
##Enter Purchase price : 4.20
##Enter selling price : 4.50
##Enter Commission : 0.01
##
##
##Stock name : RAD
##Amount paid for the stock:          $      8,400.00
##Commission paid on the purchase:    $         84.00
##Amount the stock sold for:          $      9,000.00
##Commission paid on the sale:        $         90.00
##Profit (or loss if negative):       $        426.00
##
##
##Enter your stock information? Type 'y' for yes, or 'n' for no: n
##
##
##
##Press the enter key to quit


##Output
##Test Run 5
##Enter your stock information? Type 'y' for yes, or 'n' for no: y
##
##Enter Stock name: Niantic
##Enter Number of shares : 500
##Enter Purchase price : 0.24
##Enter selling price : 1.24
##Enter Commission : 0.01
##
##
##Stock name : Niantic
##Amount paid for the stock:          $        120.00
##Commission paid on the purchase:    $          1.20
##Amount the stock sold for:          $        620.00
##Commission paid on the sale:        $          6.20
##Profit (or loss if negative):       $        492.60
##
##
##Enter your stock information? Type 'y' for yes, or 'n' for no: n
##
##
##
##Press the enter key to quit
