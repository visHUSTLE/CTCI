class Queue:
	def __init__(self):
		self.items = []

	def enqueue(self, item):
		self.items.append(item)

	def dequeue(self):
		if not self.is_empty():
			return self.items.pop(0)

	def peek(self):
		if not self.is_empty():
			return self.items[0]

	def is_empty(self):
		return len(self.items) == 0

	def __len__(self):
		return self.size()

	def size(self):
		return len(self.items)


class Node:
	def __init__(self,value):
		self.value = value
		self.left = None
		self.right = None

class BinaryTree:
	def __init__(self,root):
		self.root = Node(root)

	"""def print_tree(self, traversal_type):
		if traversal_type == "preorder":
			return self.preorder(tree.root,"")"""

	def preorder(self,start,traversal):
		if start:
			traversal += (str(start.value) + "-")
			traversal = self.preorder(start.left, traversal)
			traversal = self.preorder(start.right, traversal)
		return traversal

	def inorder(self,start,traversal):
		if start:
			traversal = self.inorder(start.left, traversal)
			traversal += str(start.value) + "-"
			traversal = self.inorder(start.right,traversal)
		return traversal

	def postorder(self,start,traversal):
		if start:
			traversal = self.postorder(start.left, traversal)
			traversal = self.postorder(start.right, traversal)
			traversal += str(start.value) + "-"
		return traversal

	def level_order(self, start):
		if start is None:
			return
		queue = Queue()
		queue.enqueue(start)
		traversal = ""
		while len(queue) > 0:
			traversal += str(queue.peek().value) + "-"
			node = queue.dequeue()

			if node.left:
				queue.enqueue(node.left)
			if node.right:
				queue.enqueue(node.right)
		return traversal

#			  1
#			/	\
#		   2     3
#         / \   / \ 
#        4   5 6   7
#

tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)

#print(tree.preorder(tree.root,""))
#print(tree.inorder(tree.root,""))
#print(tree.postorder(tree.root,""))
print(tree.level_order(tree.root))