#Is_Anagram

#Using Sorting takes O(nlogn) time complexity

#Better approach is to use dictionary
def is_Anagram(s1,s2):
	s1 = s1.replace(" ","").lower()
	s2 = s2.replace(" ","").lower()

	if len(s1) != len(s2):
		return False

	d = dict()

	for char in s1:
		if char not in d:
			d[char] = 1
		else:
			d[char] += 1
	for char in s2:
		if char not in d:
			d[char] -= 1
		else:
			d[char] -= 1

	for i in d:
		if d[i] != 0:
			return False

	return True

print(is_Anagram("fairy Tales", "rail Safety"))