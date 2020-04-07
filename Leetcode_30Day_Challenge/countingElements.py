#LC_7

#Time-O(n*n)
#n- no of elements in array

def countElements(arr):
	count = 0
	for num in arr:  #Iterating entire array takes O(n)
		if num + 1 in arr:	#checking for that num+1 in entire arr takes O(n)
			count += 1
	return count



#Approach-2 | Using dictionary
#Time complexity - O(n), Space-O(n)

def count(arr):
	d = {}
	for num in arr:
		if num not in d:
			d[num] = 1
		else:
			d[num] += 1
	count = 0
	for key, value in d.items():
		inner_count = d[key]
		while inner_count > 0:
			if key + 1 in d:
				count += 1
			inner_count -= 1	

	return count




print(countElements([1,3,2,3,5,0])) 
print(count([1,3,2,3,5,0])) 