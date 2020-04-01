def maxProfit(prices):
	if prices == []:
		return 0

	min_prices = prices[0]
	max_profit = 0
	for num in prices:
		if num <= min_prices:
			min_prices = num
		elif num - min_prices > max_profit:
			max_profit = num - min_prices
	return max_profit


print(maxProfit([4,7,1,2])) 