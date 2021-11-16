import sys
sys.path.append(sys.path[0][:-4])
import PriceCalculator
import unittest

class TestCart(unittest.TestCase):

    # @unittest.parametrize("cartPath,expected",
    #                             [
    #                                 ("../cart-json/cart-4560.json", "45.60"), 
    #                                 ("../cart-json/cart-9363.json", "93.63"), 
    #                                 ("../cart-json/cart-9500.json", "95.00"), 
    #                                 ("../cart-json/cart-11356.json", "113.56")
    #                             ]
    #                         )
    cartPath = "../cart-json/cart-4560.json"
    expected = "45.60"

    def test_execute(self):
        sys.argv = ['../PriceCalculator.py', '../cart-json/cart-4560.json',
                    '../base-prices/base-prices.json']
        main = PriceCalculator.Main()
        print(main.execute())

if __name__ == '__main__':
    unittest.main()