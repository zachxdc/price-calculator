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
