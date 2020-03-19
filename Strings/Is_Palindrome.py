#Two Approaches

#1
#Linear Time and Extra Space solution
def is_Palindrome(s):
	s = "".join([i for i in s if i.isalpha()]).replace(" ", "").lower()
	return s == s[::-1]

print(is_Palindrome("Was it a cat I Saw?"))

#Linear Time
def Is_palindrome(s):
	i = 0
	j = len(s) - 1
	while i < j:
		while not s[i].isalnum() and i < j:
			i += 1
		while not s[j].isalnum() and i < j:
			j -= 1
		if s[i].lower() != s[j].lower():
			return False
		i += 1
		j -= 1
	return True

print(Is_palindrome("Was it a cat I Saw?"))