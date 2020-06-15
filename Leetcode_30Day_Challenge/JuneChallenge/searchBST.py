#Given the root node of a binary search tree (BST) and a value. 
#You need to find the node in the BST that the node's value equals the given value. Return the subtree rooted with that node. 
#If such node doesn't exist, you should return NULL


class TreeNode:
	def __init__(self,val,left,right):
		self.val = val
		self.left = left
		self.right = right

#Iterative Approach
	def searchBST(self, root,val):
		while root != None:
			if root.val == val:
				return root
			elif val < root.val
				root = root.left
			else:
				root = root.right
		return None

#Time Complexity - O(h) where h is the height of the tree. Space - O(1)


#Recursive Approach
	def searchBST(self,root,val):
		if root is None:
			return root
		if root.val == val:
			return root
		elif val < root.val:
			return self.searchBST(root.left,val)
		else:
			return self.searchBST(root.right.val)

#Time - O(h), Space - O(1)