#LC_21


#Brute Force gives wrong answer in Leetcode because of making too many calls to binaryMatrix.get()

#Optimal Approach
#TC - O(n+m)

# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, x: int, y: int) -> int:
#    def dimensions(self) -> list[]:

class Solution:
    def leftMostColumnWithOne(binaryMatrix):
        r, c = binaryMatrix.dimensions()
        curr_row = 0
        curr_col = c-1
        while curr_row < r and curr_col >= 0:
            if binaryMatrix.get(curr_row,curr_col) == 0:
                curr_row += 1
            else:
                curr_col -= 1
        if curr_col != c-1:
            return curr_col + 1
        else:
            return -1
