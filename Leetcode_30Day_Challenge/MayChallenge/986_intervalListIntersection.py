# LC_986

#Input: A = [[0,2],[5,10],[13,23],[24,25]], B = [[1,5],[8,12],[15,24],[25,26]]
#Output: [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]


#Time and Space - O(n)
def intervalIntersection(A,B):
	i = 0
	j = 0
	merge = []
	while i < len(A) and j < len(B):
		start, end = max(A[i][0], B[j][0]), min(A[i][1], B[j][1])

		if start <= end:
			merge.append([start,end])

		if A[i][1] < B[j][1]:
			i += 1
		else:
			j += 1
	return merge


print(intervalIntersection([[0,2],[5,10],[13,23],[24,25]],[[1,5],[8,12],[15,24],[25,26]]))