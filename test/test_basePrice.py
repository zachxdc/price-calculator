import sys
sys.path.append(sys.path[0][:-4])
import basePrice
import unittest

class TestCart(unittest.TestCase):

    cart = {
        "product-type": "hoodie",
        "options": {
            "size": "small",
            "colour": "white",
        }
    }

    basePricesData = [{
        "product-type": "hoodie",
        "options": {
            "colour": ["white", "dark"],
            "size": ["small", "medium"]
        },
        "base-price": 3800
    }, {
        "product-type": "sticker",
        "options": {
            "size": ["xl"]
        },
        "base-price": 1417
    },
        {
        "product-type": "leggings",
        "options": {
        },
        "base-price": 5000
    }]

    def test_getProductPrices(self):
        self.assertEqual(basePrice.getProductPrices('hoodie', self.basePricesData) , [
            {'basePrice': 3800, 'options': ["white", "dark","small", "medium"]}]) 


    def test_getCartOptions(self):
        cart = {
            "product-type": "hoodie",
            "options": {
                "size": "small",
                "colour": "white",
            }
        }
        self.assertEqual(basePrice.getCartOptions(cart) , ['small', 'white']) 

    def test_getBasePrice(self):
        print(basePrice.getBasePrice(self.cart, self.basePricesData))
        self.assertEqual(basePrice.getBasePrice(self.cart, self.basePricesData) , 3800) 

if __name__ == '__main__':
    unittest.main()
