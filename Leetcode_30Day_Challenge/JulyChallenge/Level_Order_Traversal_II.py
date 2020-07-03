# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#Approach-1, Just traverse the level wise and reverse 
#Time - O(n) # Reversing takes O(h) time where h is number of levels. So total TC- O(n)
Space - O(1)
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return None
        res = []
        q = [root]
        while q:
            l = []
            for _ in range(len(q)):
                k = q.pop(0)
                l.append(k.val)
                if k.left:
                    q.append(k.left)
                if k.right:
                    q.append(k.right)
            res.append(l)
        return res[::-1]
