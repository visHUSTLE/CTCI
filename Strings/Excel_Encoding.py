def excelEncode(string):
	n = len(string)
	d = {'A':1, 'B':2, 'C':3}
	encode = 0
	i = n-1
	for char in string:		
		encode += (ord(char)-ord('A') + 1)*(26**(i))
		i -= 1
	return encode

print(excelEncode('ZZ'))