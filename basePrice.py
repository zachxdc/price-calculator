def getProductPrices(productType, basePricesData):
    productPricesData = []
    for item in basePricesData:
        if item['product-type'] == productType:
            options = item['options'].values()
            basePrice = item['base-price']
            allOptions = []
            for optionSet in options:
                for option in optionSet:
                    allOptions.append(option)
            productPricesData.append({
                'basePrice': basePrice,
                'options': allOptions
            })
    return productPricesData

def getCartOptions(cart):
    options = []
    for option in cart['options'].values():
        options.append(option)
    return options

def getBasePrice(cart, basePricesData):
    productType = cart['product-type']
    cartproductOptions = getCartOptions(cart)
    productPricesData = getProductPrices(productType, basePricesData)
    maxMatchCount = 0
    basePrice = productPricesData[0]['basePrice']
    for productPrice in productPricesData:
        priceOptions = productPrice['options']
        currentMatchCount = 0
        for cartproductOption in cartproductOptions:
            if cartproductOption in priceOptions:
                currentMatchCount += 1
                if currentMatchCount > maxMatchCount:
                    basePrice = productPrice['basePrice']
                    maxMatchCount = currentMatchCount
    return basePrice
