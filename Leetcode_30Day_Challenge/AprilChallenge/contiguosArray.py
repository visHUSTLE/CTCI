#LC_13
#Using HashMap
#Time - O(n), Space - O(n)

def findMaxLength(nums):
    d = {}
    maxLength = 0
    count = 0
    d[0] = -1
    
    for i in range(len(nums)):
        if nums[i] == 0:
            count += -1
        else:
            count += 1
        
        if count in d:
            maxLength = max(maxLength, i-d[count])
        else:
            d[count] = i
    return maxLength


print(findMaxLength([1,0,0,1]))