
def getUnauthorizedSellers(productListings, salesTransactions):

    authorizedSellers = {}
    unauthorizedSales = {}

    for p in productListings:
        if p['productID'] in authorizedSellers:
            authorizedSellers[p['productID']].add(p['authorizedSellerID'])
        else:
            authorizedSellers[p['productID']] = {p['authorizedSellerID']}

    for s in salesTransactions:
        if s['productID'] not in authorizedSellers or s['sellerID'] not in authorizedSellers[s['productID']]:
            if s['productID'] in unauthorizedSales:
                unauthorizedSales[s['productID']].append(s['sellerID'])
            else:
                unauthorizedSales[s['productID']] = [s['sellerID']]

    res = []
    for product, sellers in unauthorizedSales.items():
        res.append({
            "productID": product,
            "unauthorizedSellerID": sellers
        })

    return {"unauthorizedSales": res}
