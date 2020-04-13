#LC_12

#Approach -1 
#Time - O(NlogN)

def lastStoneWeight(stones):
    if len(stones) == 0:
        return 0
    if len(stones) == 1:
        return stones[-1]
    while len(stones) > 1:
        stones.sort()
        s1, s2 = stones[-1], stones[-2]
        if s1 == s2:
            stones.pop()
            stones.pop()
        else:
            s1 = abs(s1-s2)
            stones.pop()
            stones[-1] = s1
    if len(stones):
        return stones[-1]
    return 0


print(lastStoneWeight([2,7,4,1,8,1]))



#Approach -2 
#using Heaps is a better approach