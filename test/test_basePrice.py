import sys
sys.path.append(sys.path[0][:-4])
import basePrice

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


def test_getProductPrices():
    assert basePrice.getProductPrices('hoodie', basePricesData) == [
        {'basePrice': 3800, 'options': ["white", "dark","small", "medium"]}]


def test_getCartOptions():
    assert basePrice.getCartOptions(cart) == ['small', 'white']


def test_getBasePrice():
    assert basePrice.getBasePrice(cart, basePricesData)
