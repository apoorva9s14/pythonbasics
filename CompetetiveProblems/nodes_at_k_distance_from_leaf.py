# Program to print all nodes which are at
# distance k from a leaf

# utility that allocates a new Node with
# the given key
class newNode:
	def __init__(self, key):
		self.key = key
		self.left = self.right = None

# This function prints all nodes that
# are distance k from a leaf node
# path[] -. Store ancestors of a node
# visited[] -. Stores true if a node is
# printed as output. A node may be k distance
# away from many leaves, we want to print it once
def kDistantFromLeafUtil(node, path, visited,
								pathLen, k):
	
	# Base case
	if (node == None):
		return

	# append this Node to the path array
	path[pathLen] = node.key
	visited[pathLen] = False
	pathLen += 1

	# it's a leaf, so print the ancestor at
	# distance k only if the ancestor is
	# not already printed
	if (node.left == None and node.right == None and
							pathLen - k - 1 >= 0 and
							visited[pathLen - k - 1] == False):
		print(path[pathLen - k - 1], end = " ")
		visited[pathLen - k - 1] = True
		return

	# If not leaf node, recur for left
	# and right subtrees
	kDistantFromLeafUtil(node.left, path,
						visited, pathLen, k)
	kDistantFromLeafUtil(node.right, path,
						visited, pathLen, k)

# Given a binary tree and a number k,
# print all nodes that are k distant from a leaf
def printKDistantfromLeaf(node, k):
	global MAX_HEIGHT
	path = [None] * MAX_HEIGHT
	visited = [False] * MAX_HEIGHT
	kDistantFromLeafUtil(node, path, visited, 0, k)

# Driver Code
MAX_HEIGHT = 10000

# Let us create binary tree given in
# the above example
root = newNode(1)
root.left = newNode(2)
root.right = newNode(3)
root.left.left = newNode(4)
root.left.right = newNode(5)
root.right.left = newNode(6)
root.right.right = newNode(7)
root.right.left.right = newNode(8)

print("Nodes at distance 2 are:", end = " ")
printKDistantfromLeaf(root, 2)

# This code is contributed by pranchalK
