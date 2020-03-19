def excelEncode(string):
	n = len(string)
	encode = 0
	i = n-1
	for char in string:		
		encode += (ord(char)-ord('A') + 1)*(26**(i))
		i -= 1
	return encode

<<<<<<< HEAD
print(excelEncode('Z'))
=======
print(excelEncode('ZZ'))
>>>>>>> d084a6432a4c7a5b35c020bd3357bbcd5d918efa
