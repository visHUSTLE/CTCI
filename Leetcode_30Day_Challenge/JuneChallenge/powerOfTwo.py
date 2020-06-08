#Given an integer, write a function to determine if it is a power of two.
#Eg1:
	#Input: 16
	#Output: true

#Eg2:
#Input: 218
#Output: false



#Time - O(logn), Space - O(1)
def isPowerOfTwo_1(n):
	if n == 0:
		return False
	while n % 2 == 0:
		n = n//2
	return n == 1


#Using math module 
#Time - O(1), Space-O(1)
import math
def isPowerOfTwo_2(n):
	return math.log2(n) % 1 == 0 if n > 0 else False


print(isPowerOfTwo_1(8))
print(isPowerOfTwo_2(218))