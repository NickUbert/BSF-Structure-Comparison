import math
#TODO
#Update pointer to root after rotating
#keep track of number of elements in a tree with parrallel array

class Node:
    def  __init__(self, data):
        self.data = data
        self.parent = None
        self.left = None
        self.right = None
        self.bf = 0
        

class BalancedSearchForest:

def __init__(self):
	self.n = 0
	self.k = 1
	self.l = 0
	self.a = -1
	self.b = -1
	self.t = 0
	
	#directory is an array of root nodes
	self.directory = {None,None,None}
	self.treeSizes = {0,0,0}

def member(self, key):
	size = self.n

	if size is 0:
		return False

	elif size is in range(2):
		return key is self.a or key is self.b 

	elif key < self.a 
		return searchDirectory(0, key)

	elif key >= self.b
		return searchDirectory(self.k+1, key)

	#Key is within inner range
	index = getIndex(key)
	return searchDirectory(index, key)


def searchDirectory(self, index, key):
	#Check the directory index of the 
	root = self.directory[index] 
	if root is None:
		return None

	return searchTree(root,key)

def searchTree(node, key):
	#Search the AVL tree
	if node == None or key == node.data:
            return node

        if key < node.data:
            return self.searchTree(node.left, key)
        return self.searchTree(node.right, key)

def insert(self, key):
	if key<0:
		#invalid key
		return

	elif self.member(key) is not None:
		return

	size = self.n
	elif size is 0: 
		self.a, self.b = key
		self.n += 1
		return

	elif size is 1:
		# a == b when size is 1
		if key is self.a:
			return

		if key < self.a:
			self.a = key
		else:
			self.b = key

		self.n += 1

	elif size is 2:
		#at this point, endpoints are still elements 
		if key is self.a or key is self.b:
			return

		if key < self.a:
			insertInTree(0,key)
		elif key > self.b:
			insertInTree(k+1,key)

		else:
			#first inner element
			insertInTree(1,key)

	

def insertInTree(index, key):
        node =  Node(key)
        y = None
        x = self.directory[index]

        while x != None:
            y = x
            if node.data < x.data:
                x = x.left
            else:
                x = x.right

        # y is parent of x
        node.parent = y
        if node.parent is not None:
			if node.data < y.data:
            	y.left = node
        	else:
            	y.right = node

        self.treeSizes[index] += 1
        self.localUpdateBalance(node,index)


def localUpdateBalance(self, node, index):	
 	if node.bf < -1 or node.bf > 1:
    	self.localRebalance(node,index)
            return;

    if node.parent != None:
    	if node == node.parent.left:
            node.parent.bf -= 1

        	if node == node.parent.right:
        	    node.parent.bf += 1
			
			if node.parent.bf != 0:
				self.localUpdateBalance(node.parent)

def localRebalance(self, node, index):
 	if node.bf > 0:
 		if node.right.bf < 0:
 			self.localRightRotate(node.right,index)
 			self.localLeftRotate(node,index)
 		else:
 			self.localLeftRotate(node,index)
 		elif node.bf < 0:
 			if node.left.bf > 0:
 				self.localLeftRotate(node.left,index)
 				self.localRightRotate(node,index)
 			else:
 				self.localRightRotate(node,index)

  # rotate left at node x
def localLeftRotate(self, x,index):
	y = x.right
	x.right = y.left
	if y.left != None:
    	y.left.parent = x
	y.parent = x.parent;
	if x.parent == None:
		self.directory[index] = y
	elif x == x.parent.left:
		x.parent.left = y
    else:
    	x.parent.right = y

    y.left = x
    x.parent = y

        # update the balance factor
	x.bf = x.bf - 1 -treeMax(0, y.bf)
    y.bf = y.bf - 1 + treeMin(0, x.bf)

    # rotate right at node x

def localRightRotate(self, x,index):
	y = x.left
	x.left = y.right;

	if y.right != None:
		y.right.parent = x
        
	y.parent = x.parent;
	if x.parent == None:
		self.directory[index] = y
	elif x == x.parent.right:
		x.parent.right = y
	else:
		x.parent.left = y

	y.right = x
	x.parent = y

    # update the balance factor
    x.bf = x.bf + 1 - treeMin(0, y.bf)
    y.bf = y.bf + 1 + treeMax(0, x.bf)
	
def delete(self, key):
	   node = self.member(k)
        if node is None:
            return -1

        index = getIndex(key)
        self.treeSizes[index] -= 1
        root = self.directory[index]
        self.deleteNode(root,key,index)

def deleteNode(self,root,key,index):
	if root is None:
		return root

	elif key < root.data:
		root.left = self.deleteNode(root.left,key,index)
	elif key > root.data:
		root.right = self.deleteNode(root.right,key,index)
	
	else:
		if root.left is None:
			temp = root.right
			root = None
			if self.directory[index] is None:
				self.directory[index] = temp
			return temp

		elif root.right is None:
			temp = root.left
			root = None
			if self.directory[index] is None:
				self.directory[index] = temp
			return temp

		temp = self.getMinNode(root.right)
		root.data = temp.data
		root.right = self.delete(root.right,temp.data,index)


	if root is None:
		return root


	localUpdateBalance(self.directory[index])

def predecessor(self, key):
	node = member(key)

	if node is None:
		return None

	if node.parent is not None:
		if node.parent.data < key:
			return node.parent.data
	

	if node.left is not None:
		pred = treeMax(node.left)
		return pred.data
	
	else:
		index = getIndex(key)
		while index > 0:
			index -= 1 
			node = self.directory[index]
			if node is not None:
				pred = treeMax(self.directory)
				return pred.data

		return None


def successor(self, key):
	node = member(key)

	if node is None:
		return None

	if node.parent is not None:
		if node.parent.data > key:
			return node.parent.data
	

	if node.right is not None:
		pred = treeMin(node.right)
		return pred.data
	
	else:
		index = getIndex(key)
		while index < k+1:
			index += 1 
			node = self.directory[index]
			if node is not None:
				pred = treeMin(self.directory)
				return pred.data

		return None

def minimum(self, key):
	for i in range(len(self.directory)):
		node = self.directory[i]
		if node is not None:
			return treeMin(node)
	return -1

def maximum(self, key):
	for i in reversed(range(len(self.directory))):
		node = self.directory[i]
		if node is not None:
			return treeMax(node)
	return -1

#helpers
def treeMin(self, node):
	while node.left != None:
		node = node.left
	return node.data

    # find the node with the maximum key

def treeMax(self, node):
	while node.right != None:
		node = node.right
    return node.data

def getMinNode(self.node):
	while node.left != None:
		node = node.left
	return node

def getIndex(self, key):
	#PRE: key has been confirmed to be in inner range a->b
	#Add one as an offset for the lower outer tree in 0
	return ((key-self.a) // self.l) + 1



def balance(self):

def print(self):
