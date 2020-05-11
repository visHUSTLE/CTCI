#LC 997
"""
Input: N = 3, trust = [[1,3],[2,3]]
Output: 3

Input: N = 4, trust = [[1,3],[1,4],[2,3],[2,4],[4,3]]
Output: 3

"""

def findJudge(N, trust):
	#Quick Check
	if len(trust) < N-1:
		return -1

	#First cell is dummy, Indexing start from 1 to N+1
	trust_score = [0 for _ in range(N+1)]

	for p1, p2 in trust:
		trust_score[p1] -= 1	#decrease one point from p1 when p1 trusts other people
		trust_score[p2] += 1	#increase one point to p2 when p2 is trusted by others
	
	for person in range(1, N+1):
		#Town Judge will be trusted by N-1 People and town judge trusts nobody
		if trust_score[person] == N-1:
			return person
	return -1


print(findJudge(4, [[1,3],[1,4],[2,3],[2,4],[4,3]] ))

#Time and Space Complexity - O(n) 