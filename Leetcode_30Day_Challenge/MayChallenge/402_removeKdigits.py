# LC_402
#Input: num = "1432219",3, k = 3
#Output: "1219"


#Stack Approach

def removeKdigits(nums, k):
	stack = []
	for num in nums:
		#Pop the element from the stack if the current element is smaller than last added element to stack
		while k and stack and num < stack[-1]:
			stack.pop()
			k -= 1
		stack.append(num)
	
	#if the traversal is complete and stack is filled with all the nums but still k elements left to remove.
	while k>0:
		stack.pop()
		k -= 1
	output = "".join(stack).lstrip("0")	#Using lstrip to remove trailing zeroes
	return (output if output else "0")


print(removeKdigits("41353246", 4))
