#Given an array with n objects colored red, white or blue, 
#sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white and blue.
#Ex 1 
	#Input: [2,0,2,1,1,0]
	#Output: [0,0,1,1,2,2]


#using inbuilt sort takes time complexity - O(nlogn)

#Using Two pass Approach takes Time - 2*O(n), Space - O(1)
def sortColors(nums):
	zeros, ones, twos = 0,0,0
	for num in nums:
		if num == 0:
			zeros += 1
		elif num == 1:
			ones += 1
		else:
			twos += 1
	for num in nums:
		if num == 0:
			num = 0
			zeros -= 1
		elif num == 1:
			num = 1
			ones -= 1
		else:
			num == 2
			num = 2
			twos -= 1


#Using three-pointers takes Time - O(n)
def sortColors1(nums):
	l,cur, r = 0, 0, len(nums)-1
	while cur <= r:
		if nums[cur] == 0:
			nums[l], nums[cur] = nums[cur], nums[l]
		elif nums[cur] == 2:
			nums[cur], nums[r], nums[r], nums[cur]
		else:
			cur += 1

print(sortColors([2,0,2,1,1,0]))
print(sortColors1([2,0,2,1,1,0]))