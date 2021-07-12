def maximumToys(prices, k):
    # Write your code here
    prices.sort()
    for i in range(len(prices)):
        k = k - prices[i]
        if k < 0:
            return i
    return prices.length
