#LC_901
#As usual, Brute Force will give TLE

#Using Stack Approach 
#TC - O(n), Space - O(n)
class StockSpanner:

    def __init__(self):
        self.stocks = []
        

    def next(self, price: int) -> int:
        span = 1
        while self.stocks and self.stocks[-1][0] <= price:
            span = span + self.stocks.pop()[1]
        self.stocks.append([price,span])
        return span


# Your StockSpanner object will be instantiated and called as such:
obj = StockSpanner()
param_1 = obj.next(100)
param_2 = obj.next(80)
param_3 = obj.next(60)
param_4 = obj.next(70)
print(param_4)
