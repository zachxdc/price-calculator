import sys
sys.path.append(sys.path[0][:-4])
import cart
import unittest

class TestCart(unittest.TestCase):

    # initialise the testing data
    cartData = [
        {
            "product-type": "hoodie",
            "options": {
                "size": "small",
                "colour": "white",
                "print-location": "front"
            },
            "artist-markup": 20,
            "quantity": 1
        }
    ]

    basePricesData = [
        {
            "product-type": "hoodie",
            "options": {
                "colour": ["white", "dark"],
                "size": ["small", "medium"]
            },
            "base-price": 3800
        },
        {
            "product-type": "hoodie",
            "options": {
                "size": ["large"],
                "colour": ["white"]
            },
            "base-price": 3848
        },
        {
            "product-type": "sticker",
            "options": {
                "size": ["small"]
            },
            "base-price": 221
        },
        {
            "product-type": "leggings",
            "options": {
            },
            "base-price": 5000
        }
    ]

    # test each function then check if the return value matches the expected result
    def test_getOneProductPrice(self):
        self.assertEqual(cart.Cart(self.cartData, self.basePricesData).getOneProductPrice(self.cartData[0], 3800), 4560)

    def test_getCartTotalPrices(self):
        self.assertEqual(cart.Cart(self.cartData, self.basePricesData).getCartTotalPrice(), '45.60')

if __name__ == '__main__':
    unittest.main()