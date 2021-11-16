from basePrice import getBasePrice

class Cart:
    def __init__(self, cartData, basePricesData):
        self.cartData = cartData
        self.basePricesData = basePricesData
    
    def getOneProductPrice(self, cart, basePrice):
        markup = cart['artist-markup'] / 100
        quantity = cart['quantity']
        price = (basePrice + round(basePrice * markup)) * quantity
        return price

    def getCartTotalPrice(self):
        result = 0
        for cart in self.cartData:
            basePrice = getBasePrice(cart, self.basePricesData)
            price = self.getOneProductPrice(cart, basePrice)
            result += price
        result = format(result / 100, '.2f')
        return result