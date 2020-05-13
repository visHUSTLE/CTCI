# LC_540
"""Input: [1,1,2,3,3,4,4,8,8]
Output: 2"""

#Your solution should run in O(log n) time and O(1) space.

#Approach-1 #Time-O(n), Space-O(1)
def singleNonDuplicate(nums):
	#Looping through the array with a step of 2 till len(nums)-2
	for i in range(0, len(nums)-2, 2):
		if nums[i] != nums[i+1]:
			return nums[i]
	return nums[-1]


#Approach-2 
#Binary Search #Time-O(logn), Space-O(1)
def singleNonDuplicate1(nums):
	left, right = 0, len(nums)-1
	while left < right:
		mid = left + (right-left)//2
		if nums[mid] == nums[mid+1]:
			if mid % 2 == 0:	#if this condition is true, there are even no.of elements on both sides of mid.
				#Since nums[mid] == nums[mid+1] we can disregard the left portion of mid and change the left postion  
				left = mid + 2
			else:	#that ,means there are odd no.of elements on both sides of mid.
				#Since nums[mid] == nums[mid+1], we can disregard the right portion of mid
				right = mid - 1
		elif nums[mid] == nums[mid-1]:
			if mid % 2 == 0:
				right = mid - 2
			else:
				left = mid + 1
		else:
			return nums[mid]
	return nums[left]

       

print(singleNonDuplicate1([1,1,2,3,3,4,4,8,8]))