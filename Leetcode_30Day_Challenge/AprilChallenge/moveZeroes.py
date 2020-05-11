#LC-4

#Using Two-Pointer Approach 
#Time-O(n), Space- O(n)

def moveZeroes(nums):
	i = 0
	j = 0
	for i in range(len(nums)):
		if nums[i] != 0:
			nums[i], nums[j] = nums[j], nums[i]
			j += 1
	return nums

print(moveZeroes([0,1,0,3,12]))