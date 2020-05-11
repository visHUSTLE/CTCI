#Brilliant Solution I learnt from leetcode 
#Using dictionary takes O(n) space complexity but XOR gives Linear run time and constant space


def singleNumber(nums):
	i = 0
	for num in nums:
		i ^= num
	return i

print(singleNumber([4,1,2,1,2]))