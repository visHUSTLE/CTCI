# LC_208
#Implementing Trie Data Structure

class TreeNode:
	def __init__(self,val):
		self.val = val
		self.children = {}
		self.end = False

class Trie:
	def __init__(self):
		self.root = TreeNode(None)

	def insert(self,word):
		parent = self.root
		for i, char in enumerate(word):
			if char not in parent.children:
				parent.children[char] = TreeNode(char)
			parent = parent.children[char]
		if i == len(word)-1:
			parent.end = True

	def search(self,word):
		parent = self.root
		for char in word:
			if char not in parent.children:
				return False
			parent = parent.children[char]
		return parent.end

	def startsWith(self,word):
		parent = self.root
		for char in word:
			if char not in parent.children:
				return False
			parent = parent.children[char]
		return True


t = Trie()
t.insert("apple")
t.search("apple")
t.search("app")
t.startsWith("app")
