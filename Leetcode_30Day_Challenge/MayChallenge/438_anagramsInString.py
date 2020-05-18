# LC_438
#Input:s: "cbaebabacd" p: "abc"

#Output:[0, 6]

#Time- O(n), Space -O(n)

from collections import Counter
def findAnagrams(s,p):
    s_len = len(s)
    p_len = len(p)
    if s_len < p_len:
    	return []
    s_count = Counter()
    p_count = Counter(p)

    result = []
    for i in range(s_len):
    	s_count[s[i]] += 1
    	if i >= p_len:
    		if s_count[s[i - p_len]] == 1:
    			del s_count[s[i - p_len]]
    		else:
    			s_count[s[i - p_len]] -= 1
    	if p_count == s_count:
    		result.append(i-p_len+1)
    return result

print(findAnagrams("cbaebabacd","abc"))

