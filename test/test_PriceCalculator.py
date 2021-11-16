import sys
sys.path.append(sys.path[0][:-4])
import PriceCalculator
import unittest
import os

class TestCart(unittest.TestCase):

    priceCalculatorPath = os.getcwd() + '/PriceCalculator.py'
    basePricesPath = os.getcwd() + '/base-prices/base-prices.json'
    print(basePricesPath)
    print(priceCalculatorPath)
    cartPath4560 = os.getcwd() + '/cart-json/cart-4560.json'
    cartPath9363 = os.getcwd() + '/cart-json/cart-9363.json'
    cartPath9500 = os.getcwd() + '/cart-json/cart-9500.json'
    cartPath11356 = os.getcwd() + '/cart-json/cart-11356.json'

    def test_execute(self):
        sys.argv = ['/Users/zach/Redbubble测试/重要备份/price-calculator/test/test_PriceCalculator.py', '/Users/zach/Redbubble测试/重要备份/price-calculator/cart-json/cart-4560.json', '/Users/zach/Redbubble测试/重要备份/price-calculator/base-prices/base-prices.json']
        main = PriceCalculator.Main()
        self.assertEqual(main.execute(), '45.60')
    
    # def test_execute_cart_9363(self):
    #     sys.argv = [self.priceCalculatorPath, self.cartPath9363, self.basePricesPath]
    #     main = PriceCalculator.Main()
    #     self.assertEqual(main.execute(), 93.63)

    # def test_execute_cart_9500(self):
    #     sys.argv = [self.priceCalculatorPath, self.cartPath9500, self.basePricesPath]
    #     main = PriceCalculator.Main()
    #     self.assertEqual(main.execute(), 95.00)

    # def test_execute_cart_11356(self):
    #     sys.argv = [self.priceCalculatorPath, self.cartPath11356, self.basePricesPath]
    #     main = PriceCalculator.Main()
    #     self.assertEqual(main.execute(), 113.56)

if __name__ == '__main__':
    unittest.main()