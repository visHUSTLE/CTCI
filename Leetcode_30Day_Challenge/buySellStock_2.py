#Variation of Buy and Sell Stock 1 Problem

#Time - O(n), Space- O(1)

def stockProfit(prices):
	min_price = prices[0]
	maxProfit = 0
	for i in range(len(prices)):
		if prices[i] <= min_price:
			min_price = prices[i]

		elif prices[i] - min_price > 0:
			maxProfit += prices[i] - min_price
			min_price = prices[i]

	return maxProfit

print(stockProfit([1,2,3,4,5]))