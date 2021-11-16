import sys
sys.path.append(sys.path[0][:-4])
import PriceCalculator
import unittest
import os

class TestCart(unittest.TestCase):

    # set the path to make program path be adapatable for different OSs
    priceCalculatorPath = os.getcwd() + '/PriceCalculator.py'
    basePricesPath = os.getcwd() + '/base-prices/base-prices.json'

    # initialise the testing data
    cart = [
        { "path": os.getcwd() + '/cart-json/cart-4560.json', "expectedResult": "45.60" },
        { "path": os.getcwd() + '/cart-json/cart-9363.json', "expectedResult": "93.63" },
        { "path": os.getcwd() + '/cart-json/cart-9500.json', "expectedResult": "95.00" },
        { "path": os.getcwd() + '/cart-json/cart-11356.json', "expectedResult": "113.56" }
    ]

    # use loop to test all cart data, then check if the return match the expected value
    def test_execute(self):
        for i in range(0, len(self.cart)):
            sys.argv = [self.priceCalculatorPath, self.cart[i]['path'], self.basePricesPath]
            main = PriceCalculator.Main()
            self.assertEqual(main.execute(), self.cart[i]['expectedResult'])

if __name__ == '__main__':
    unittest.main()