# LC_567

#Input: s1 = "ab" s2 = "eidbaooo"
#Output: True
#Explanation: s2 contains one permutation of s1 ("ba").


#Using Sliding Window Technique
#Time - O(n), Space- O(n)
from collections import Counter
def checkInclusion(s1,s2):
	if len(s1) > len(s2):
		return False
	s1_count = Counter(s1)
	win_count = Counter()
	for i,c in enumerate(s2):
		win_count[c] += 1
		if i >= len(s1):
			left_elem = s2[i-len(s1)]
			if win_count[left_elem] == 1:
				del win_count[left_elem]
			else:
				win_count[left_elem] -= 1
		if s1_count == win_count:
			return True
	return False

print(checkInclusion("ab","eidboaoo"))