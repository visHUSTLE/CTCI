#Leetcode #387

def firstUniqChar(s):
    d = {}
    for char in s:
        if char not in d:
            d[char] = 1
        else:
            d[char] += 1
    for i in range(len(s)):
        if s[i] in d and d[s[i]] == 1:
            return i
    return -1

print(firstUniqChar("loveleetcode"))