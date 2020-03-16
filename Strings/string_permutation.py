def is_permut(s1,s2):
	s1 = s1.replace(" ", "")
	s2 = s2.replace(" ", "")

	if len(s1) != len(s2):
		return False

	d = {}
	for char in s1:
		if char in d:
			d[char] += 1
		else:
			d[char] = 1
	for char in s2:
		if char in d:
			d[char] -= 1
		else:
			d[char] = 1

	return all(value == 0 for value in d.values())



print(is_permut('dreiving','drrrring'))