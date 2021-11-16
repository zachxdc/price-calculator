import sys
sys.path.append(sys.path[0][:-4])
import cart

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

cart_ = cart.Cart(cartData, basePricesData)


def test_getOneProductPrice():
    assert cart_.getOneProductPrice(cartData[0], 3800) == 4560


def test_getCartTotalPrices():
    assert cart_.getCartTotalPrice() == '45.60'
