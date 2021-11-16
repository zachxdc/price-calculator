from basePrice import getBasePrice

class Cart:
    #initialise a cart object
    def __init__(self, cartData, basePricesData):
        self.cartData = cartData
        self.basePricesData = basePricesData

    """
	This function is to calculate the total price for total price for one single items in the cart
	Parameters:
		cart: A cart object that is read from the JSON
		basePrice: A base price for a single specific item
	Note: Make sure pricedict's add_base_price() is called at least once
		before calling calculate()
	Returns: Total price of single items in the cart.
	"""
    
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
            result += price
        result = format(result / 100, '.2f')
        return result