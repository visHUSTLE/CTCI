#Google Interview Question

#Approach 1 
#Time - O(1), Space - O(n)

def isHappy(n):
	seen = set()
	while n != 1:
		current =  n
		sum = 0
		while current != 0:
			sum += (current % 10) *(current % 10)
			current //= 10
		if sum in seen:
			return False
		seen.add(sum)
		n = sum
	return True

print(isHappy(19))