# Node class
class Node:
	
	# Function to initialise the node object
	def __init__(self, data):
		self.data = data # Assign data
		self.next = None # Initialize next as null
	
# Linked List class contains a Node object
class LinkedList:
	
	# Function to initialize head
	def __init__(self):
		self.head = None

	# Function to insert a new node at the beginning
	def push(self, new_data):
		new_node = Node(new_data)
		new_node.next = self.head
		self.head = new_node

	# Print the linked list
	def printList(self):
		node = self.head
		while node:
			print(str(node.data) + "->", end = "")
			node = node.next
		print("NULL")

	# Function to get the middle of
	# the linked list
	def printMiddle(self):
		count = 0
		mid = self.head
		heads = self.head

		while(heads != None):
	
		# Update mid, when 'count'
		# is odd number
			if count&1:
				mid = mid.next
			count += 1
			heads = heads.next
			
		# If empty list is provided
		if mid!=None:
			print("The middle element is ", mid.data)

# Code execution starts here
if __name__=='__main__':
	
	# Start with the empty list
	llist = LinkedList()
	
	for i in range(5, 0, -1):
		llist.push(i)
	llist.printList()
	llist.printMiddle()

# This Code is contributed by Manisha_Ediga
