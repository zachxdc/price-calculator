import sys
import cart
from readDataFile import readDataFile

class Main:
    def __init__(self):
        self.checkParams()

    def checkParams(self):
        # check parameters are correct when the program is running
        if not len(sys.argv) != 3:
            self.cartPath = sys.argv[1]
            self.basePricesPath = sys.argv[2]
        else:
            print('Please provide command as: python [PriceCalculator-path] [cart-path] [base-prices-path]')
            sys.exit(0)

    def execute(self):
        # Get cart data and base price data by reading JSON files
        self.cartData = readDataFile(self.cartPath)
        self.basePricesData = readDataFile(self.basePricesPath)
        self.cart = cart.Cart(self.cartData, self.basePricesData)
        # Call function to calculate the total price for cart
        self.result = self.cart.getCartTotalPrice()
        print(self.result)
    
#
if __name__ == '__main__':
    main = Main()
    main.execute()