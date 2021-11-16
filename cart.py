from basePrice import getBasePrice

class Cart:
    def __init__(self, cartData, basePricesData):
        self.cartData = cartData
        self.basePricesData = basePricesData

    def getCartTotalPrice(self):
        result = 0
        for cart in self.cartData:
            basePrice = getBasePrice(cart, self.basePricesData)
            price = self.getOneProductPrice(cart, basePrice)
            result += price
        result = format(result / 100, '.2f')
        return result