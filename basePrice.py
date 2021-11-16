# get all base prices for different product options
def getProductPrices(productType, basePricesData):
    # define a array to save base price and product options
    productPricesData = []
    # look through all price data, get a price for each item
    for item in basePricesData:
        # match the product type
        if item['product-type'] == productType:
            options = item['options'].values()
            basePrice = item['base-price']
            allOptions = []
            # Extract detailed option
            for optionSet in options:
                for option in optionSet:
                    # save possible product options
                    allOptions.append(option)
            # saved all product options and based price from basePrice.json, used for get data later
            productPricesData.append({
                'basePrice': basePrice,
                'options': allOptions
            })
    return productPricesData

# get option for each product in the cart
def getCartOptions(cart):
    options = []
    for option in cart['options'].values():
        options.append(option)
    return options

# get base price for a single product
def getBasePrice(cart, basePricesData):
    # match the product type
    productType = cart['product-type']
    # get all options for all products in the cart
    cartProductOptions = getCartOptions(cart)
    # get all product prices for all options
    productPricesData = getProductPrices(productType, basePricesData)
    maxMatchCount = 0
    # set initial base price to avoid loss of base price
    basePrice = productPricesData[0]['basePrice']
    # look through each product with a specific option in all product price data
    for productPrice in productPricesData:
        # get the all possible options as a list
        priceOptions = productPrice['options']
        currentMatchCount = 0
        # match the price option with the carted product option to get the base price
        for cartProductOption in cartProductOptions:
            # check the option of products in cart matches with the options in JSON file
            if cartProductOption in priceOptions:
                currentMatchCount += 1
                # track whether the product matches the most properties
                if currentMatchCount > maxMatchCount:
                    basePrice = productPrice['basePrice']
                    maxMatchCount = currentMatchCount
    return basePrice
