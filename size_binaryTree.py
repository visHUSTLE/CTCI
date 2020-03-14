#The size of a tree is the total number of nodes in the tree.

class Stack:
	def __init__(self):
		self.items = []

	def push(self,item):
		self.items.append(item)

	def pop(self):
		if not self.is_empty():
			return self.items.pop()
	
	def peek(self):
		if not self.is_empty():
			return self.items[len(items)-1]

	def is_empty(self):
		return len(self.items) == 0

	def __len__(self):
		return self.size()

	def size(self):
		return len(self.items)



class Node:
	def __init__(self, value):
		self.value = value
		self.left = None
		self.right = None

class BinaryTree:
	def __init__(self,root):
		self.root = Node(root)

	def size(self):
		if self.root is None:
			return 0
		s = Stack()
		s.push(self.root)
		size = 1
		while s:
			node = s.pop()
			if node.left:
				size += 1
				s.push(node.left)
			if node.right:
				size += 1
				s.push(node.right)
		return size

	def size_recursive(self, node):
		if node is None:
			return 0
		left_size = self.size_recursive(node.left)
		right_size = self.size_recursive(node.right)
		return 1 + left_size + right_size 

tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)


print(tree.size())
print(tree.size_recursive(tree.root))
