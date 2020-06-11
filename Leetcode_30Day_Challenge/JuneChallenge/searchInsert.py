#Given a sorted array and a target value, 
#return the index if the target is found. If not, return the index where it would be if it were inserted in order.

#Eg 1
	#Input: [1,3,5,6], 5
	#Output: 2



def searchInsert(nums, target):
	lo,hi = 0, len(nums)-1
	while lo < hi:
		mid = lo+(hi-lo)//2
		if nums[mid] == target:
			return mid
		elif nums[mid] < target:
			lo = mid+1
		else:
			hi = mid
	if lo == len(nums)-1 and target>nums[-1]:
		return len(nums)
	return lo

print(searchInsert([1,3,5,6], 7))
