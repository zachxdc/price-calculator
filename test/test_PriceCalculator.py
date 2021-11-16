import sys
sys.path.append(sys.path[0][:-4])
import PriceCalculator
import unittest
import os

class TestCart(unittest.TestCase):

    priceCalculatorPath = os.getcwd() + '/PriceCalculator.py'
    basePricesPath = os.getcwd() + '/base-prices/base-prices.json'

    cart = [
        { "path": os.getcwd() + '/cart-json/cart-4560.json', "expectedResult": "45.60" },
        { "path": os.getcwd() + '/cart-json/cart-9363.json', "expectedResult": "93.63" },
        { "path": os.getcwd() + '/cart-json/cart-9500.json', "expectedResult": "95.00" },
        { "path": os.getcwd() + '/cart-json/cart-11356.json', "expectedResult": "113.56" }
    ]

    def test_execute(self):
        for i in range(0, len(self.cart)):
            sys.argv = [self.priceCalculatorPath, self.cart[i]['path'], self.basePricesPath]
            main = PriceCalculator.Main()
            self.assertEqual(main.execute(), self.cart[i]['expectedResult'])

if __name__ == '__main__':
    unittest.main()