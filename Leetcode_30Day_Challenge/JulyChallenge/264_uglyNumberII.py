#Naive Approach
#Gives TLE ,need to come up with better Approach



class Solution:
    def nthUglyNumber(self, n: int) -> int:
        num = 0
        while n > 0:
            num += 1
            if self.isUgly(num):
                n -= 1
        return num
        
    def isUgly(self, num):
        if num < 1:
            return False
        while num%2 == 0 or num%3 == 0 or num%5 == 0:
            for i in [2,3,5]:
                if num % i == 0:
                    num /= i
        return num == 1
