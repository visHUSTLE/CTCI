#Given two strings S and T, return if they are equal when both are typed into empty text editors. 
# means a backspace character.


"""Input: S = "ab#c", T = "ad#c"
Output: true
Explanation: Both S and T become "ac"."""

#Approach -1 
#Time - O(n). Space -O(n)

def backspaceCompare(S,T):
	S_New = []
	for char in S:
		if char != '#':
			S_New.append(char)
		else:
			if S_New != []:
				S_New.pop()

	T_New = []
	for char in T:
		if char != '#':
			T_New.append(char)
		else:
			if T_New != []:
				T_New.pop()

	return S_New == T_New


print(backspaceCompare("a##c", "#a#c"))




