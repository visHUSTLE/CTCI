# LC_451
#Input:"tree"
#Output:"eert"



#Time and Space - O(n)

from collections import Counter
def frequencySort(s):
	result = ''
	count = Counter(s)
	sort_count = sorted(count, key=lambda x:count[x],reverse =True)
	for char in sort_count:
		result += char*count[char]
	return result



print(frequencySort('Aabb'))

