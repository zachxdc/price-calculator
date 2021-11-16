from basePrice import getBasePrice

class Cart:
    #initialise a cart object
    def __init__(self, cartData, basePricesData):
        self.cartData = cartData
        self.basePricesData = basePricesData
    
    # function for getting total price for a single cart
    def getOneProductPrice(self, cart, basePrice):
        markup = cart['artist-markup'] / 100
        quantity = cart['quantity']
        price = (basePrice + round(basePrice * markup)) * quantity
        return price

    def getCartTotalPrice(self):
        result = 0
        #loop for looking through all items in cart
        for cart in self.cartData:
            # get basePrice
            basePrice = getBasePrice(cart, self.basePricesData)
            # get total price
            price = self.getOneProductPrice(cart, basePrice)
            # Add result to current total price
            result += price
        result = format(result / 100, '.2f')
        return result