LC_951

#Brute Force approach, this will lead to TLE.
#Need to think of a better Approach


class Solution:
    def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:
        for i in range(N):
            cells = self.nextDaycells(cells)
        return cells
        
    def nextDaycells(self,cells):
        res = [0]*len(cells)
        for i in range(1, len(cells)-1):
            if (cells[i-1] == 0 and cells[i+1] == 0) or (cells[i-1] == 1 and cells[i+1] == 1):
                res[i] = 1
        return res
