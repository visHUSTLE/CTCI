#Given a string s and a string t, check if s is subsequence of t.
#Ex 1 -
	#Input: s = "abc", t = "ahbgdc"
	#Output: true
#Ex2-
	#Input: s = "axc", t = "ahbgdc"
	#Output: false


#Time - O(n), Space- O(1)
def isSubsequence(s,t):
	i = 0
	j = 0
	while i < len(s) and j < len(t):
		if s[i] == t[j]:
			i += 1
			j += 1
		j += 1
	return i == len(s)


print(isSubsequence("abc","ahbgdc"))
print(isSubsequence("axc","ahbgdc"))