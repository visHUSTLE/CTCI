def groupAnagrams(strs):
    out = []
    d = {}
    for word in strs:
        word1 = ''.join(sorted(word))
        if word1 not in d:
            d[word1] = [word]
        else:
            d[word1].append(word)
    for key,value in d.items():
        out.append(d[key])
    return out


print(groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))