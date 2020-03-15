def is_Unique(string):
	return len(string.lower()) == len(set(string.lower()))

print(is_Unique('bEAR'))
print(is_Unique('Unique'))