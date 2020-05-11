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


#Approach 2
#Space - O(1)

"""def numSquare(n):
	sum = 0
	while n:
		sum += (n % 10) * (n % 10)
		n //= 10
	return sum

def isHappy_1(n):
	slow = n
	fast = n
	while True:
		slow = numSquare(slow)
		fast = numSquare(numSquare(fast))

		if (slow != fast):
			continue
		else:
			break

	return slow == 1

print(isHappy_1(82))"""