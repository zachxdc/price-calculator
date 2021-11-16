import sys
from readDataFile import readDataFile

class Main:
    def __init__(self):
        self.checkParams()

    def checkParams(self):
        if not len(sys.argv) != 3:
            self.cartPath = sys.argv[1]
            self.basePricesPath = sys.argv[2]
        else:
            print('Please provide command as: python [PriceCalculator-path] [cart-path] [base-prices-path]')
            sys.exit(0)

    def execute(self):
        self.cartData = readDataFile(self.cartPath)
        self.basePricesData = readDataFile(self.basePricesPath)
    
#
if __name__ == '__main__':
    main = Main()
    main.execute()