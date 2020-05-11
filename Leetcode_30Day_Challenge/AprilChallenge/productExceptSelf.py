#LC_15
#Time and Space - O(n)


def productExceptSelf(nums):
	A = [0]*len(nums)
	productLeft = 1
	for i in range(len(nums)):
		A[i] = productLeft
		productLeft *= nums[i]

	B = [0]*len(nums)
	productRight = 1
	for j in range(len(nums)-1, -1,-1):
		B[j] = productRight
		productRight *= nums[j]

	result = []
	for i in range(len(A)):
		result.append(A[i]*B[i])

	return result

print(productExceptSelf([1,2,3,4]))