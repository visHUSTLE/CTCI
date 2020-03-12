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

class Queue:
	def __init__(self):
		self.items = []

	def enqueue(self,item):
		self.items.append(item)

	def dequeue(self):
		if not self.is_empty():
			return self.items.pop(0)

	def peek(self):
		if not is_empty():
			return self.items[0]

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


	def reverse_level_order(self,start):		
		if start is None:
			return
		q = Queue()
		s = Stack()
		q.enqueue(start)
		traversal = ""
		while len(q) > 0:			
			node = q.dequeue()
			s.push(node)

			if node.right:
				q.enqueue(node.right)
			if node.left:
				q.enqueue(node.left)
		while len(s) > 0:
			traversal += str(s.pop().value) + "-"
		return traversal

tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)


print(tree.reverse_level_order(tree.root))