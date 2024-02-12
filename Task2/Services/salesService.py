
"""
    Implementation of algorithm to verify sales.
    Returning object containing list of unauthorized sales
"""
def getUnauthorizedSellers(productListings, salesTransactions):

    # Initialization of auxiliary dictionaries
    authorizedSellers = {}
    unauthorizedSales = {}

    # Store authorized sellers for each product in hash map
    # So we don't have to iterate over a 'productListings' list each time when checking sales transactions
    for p in productListings:
        if p['productID'] in authorizedSellers:
            authorizedSellers[p['productID']].add(p['authorizedSellerID'])
        else:
            authorizedSellers[p['productID']] = {p['authorizedSellerID']}

    # Check if sale is authorized and if not, store seller ID in hash map for each product
    # This hash map will contain result data, but we need to transform it in defined shape before returning
    for s in salesTransactions:
        if s['productID'] not in authorizedSellers or s['sellerID'] not in authorizedSellers[s['productID']]:
            if s['productID'] in unauthorizedSales:
                unauthorizedSales[s['productID']].append(s['sellerID'])
            else:
                unauthorizedSales[s['productID']] = [s['sellerID']]

    # List containing resulting unauthorized sales
    res = []

    # For each unauthorized sale that we found, add it to resulting list in defined shape
    for product, sellers in unauthorizedSales.items():
        res.append({
            "productID": product,
            "unauthorizedSellerID": sellers
        })

    return {"unauthorizedSales": res}
