#Approach-1
#Time Complexity - O(n)

def maxSubarray(nums):
	sum = nums[0]
	maxSum = nums[0]
	for i in range(1, len(nums)):
		sum = max(sum+nums[i], nums[i])
		maxSum = max(sum, maxSum)
	return maxSum

print(maxSubarray([-2,1,-3,4,-1,2,1,-5,4]))