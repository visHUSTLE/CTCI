# LC_230

#Input: root = [3,1,4,null,2], k = 1
#   3
#  / \
# 1   4
#  \
#   2
#Output: 1


#Approach - Inorder Traversal gives elements in Ascending order
#Time and Space - O(n)


# Definition for a binary tree node.
class TreeNode:
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right

class Solution:
	def kthSmallest(self, root, k):
		elements = []
		
		def inOrder(root):
			if root:
				left = inOrder(root.left)
				elements.append(root.val)
				right = inOrder(root.right)
		
		inOrder(root)
		return elements[k-1]



