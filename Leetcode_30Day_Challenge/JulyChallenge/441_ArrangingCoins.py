#You have a total of n coins that you want to form in a staircase shape, where every k-th row must have exactly k coins.
#Given n, find the total number of full staircase rows that can be formed.


#Appraoch - 1 
#Time - O(n), Space - O(1)
def arrangeCoins(n):
	row = 1
	while n>0:
		if row <= n:
			n -= row
			row += 1
		else:
			break
	return row-1


#Approach - 2 , Binary Search (Using the concept of 1+2+3+....k = k(k+1)/2 <= n)
#Time - O(logn), Space - O(1)
def Arrangecoins(n):
	l, r = 0, n
	while l<=r:
		k = (l+r)//2
		curr_sum = k*(k+1)//2
		if curr_sum == n:
			return k
		elif curr_sum > n:
			r = k-1
		else:
			l = k+1
	return r


print(arrangeCoins(42))
print(Arrangecoins(42))
		
