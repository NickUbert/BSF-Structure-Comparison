import math
#Enums
empty_rating = -2
low_rating = 0
med_rating = 1
high_rating = 2
full_rating = 5

low_adj = 1
med_adj = 2
large_adj = 3


class Node:
    def  __init__(self, data):
        self.data = data
        self.parent = None
        self.left = None
        self.right = None
        self.bf = 0

class BalancedSearchForest:

	def __init__(self):
		self.directory = [None,None,None]
		self.treeSizes = [0,0,0]
		self.a = 0
		self.b = 0
		self.t = 1
		self.k = 1
		self.l = 1
		self.n = 0
		self.lockedL = False

	def insert(self, key):
		if key<0:
			return

		if self.member(key) is not None:
			return

		#starting out
		size = self.n
		if size == 0:
			self.a = key
			self.insertInTree(1, key)

		elif size == 1:
			if key < self.a:
				self.b = self.a
				self.a = key
				self.insertInTree(1,key)

			else:
				self.b = key
				self.insertInTree(2,key)

			self.l = self.b - self.a

		else:
				index = self.getIndex(key)
				self.insertInTree(index, key)

	def member(self, key):
		return None

	def balance(self):
		self.lockedL = False
		treeRatings = [0]*(self.k+2)

		#Interpret Phase
		for i in range(self.k+2):
			treeRatings[i] = self.treeRating(i)

		#Partition Phase

		sectionSize = math.ceil((self.k + 2)/4)
		sections = [0,0,0]
		index = 0
		while index < sectionSize:
			sections[0] += treeRatings[index]
			index += 1

		while index < (self.k+2)-sectionSize:
			sections[1] += treeRatings[index]
			index += 1

		while index < self.k+2:
			sections[2] += treeRatings[index]
			index += 1

		sections[0] /= sectionSize
		sections[1] /= (self.k+2)-sectionSize
		sections[2] /= sectionSize

		#Restructure Phase
		if sections[0] >= full_rating/3:
			self.adjustA(large_adj)
		elif sections[0] >= full_rating/4:
			self.adjustA(med_adj)
		elif sections[0] == empty_rating:
			self.adjustA(-1 * large_adj)
		else:
			self.adjustA(low_adj)
		
		if sections[2] >= full_rating/3:
			self.adjustB(large_adj)
		elif sections[2] >= full_rating/4:
			self.adjustB(med_adj)
		elif sections[2] == empty_rating:
			self.adjustB(-1 * low_adj)
		else:
			self.adjustB(med_adj)

		if not self.lockedL:
			if sections[1] >= full_rating/2:
				self.adjustL(large_adj)
			elif sections[1] >= full_rating/3:
				self.adjustL(med_adj)
			elif sections[1] == empty_rating:
				self.adjustL(-1 * large_adj)
			else:
				self.adjustL(low_adj)

		#Reassign
		#Increase directory AND treesizes
		displacements = []
		for i in range(len(self.directory)):
			if self.directory[i] is not None:
				keys = self.validateNodes(i)
				for key in keys:
					displacements.append(key)

		print("DIS:",displacements)
		newDir = [None] * (self.k+2)
		newSizes = [0] * (self.k+2)
		for i in range(min(self.k+2,len(self.directory))):
			newDir[i] = self.directory[i]
			newSizes[i] = self.treeSizes[i]

		self.directory = newDir
		self.treeSizes = newSizes

		for key in displacements:
			newIndex = self.getIndex(key)
			self.insertInTree(newIndex,key)

	def treeRating(self, index):
		size = self.treeSizes[index]
		rangeSize = self.t // 3
		if size == 0:
			return empty_rating

		elif size >= self.t:
			return full_rating

		elif size >= (self.t-rangeSize):
			return high_rating

		elif size >= (self.t-(2*rangeSize)):
			return med_rating

		else:
			return low_rating



	#Helpers
	def getIndex(self, key):
		#pre: key is unique, valid, and within a and b 
		if key < self.a:
			return 0

		if key >= self.b:
			return self.k+1

		return ((key-self.a) // self.l) + 1 

	def incrementTreeSize(self, index):
		self.treeSizes[index] += 1

	def decrementTreeSize(self, index):
		self.treeSizes[index]-= 1

	def incrementForestSize(self):
		self.n += 1
		self.t = math.floor(math.log2(self.n))

	def decrementForestSize(self):
		self.n -= 1
		self.t = math.floor(math.log2(self.n)) 

	def adjustA(self, degree):
		self.a -= (self.l * degree)
		if self.a < 0:
			self.a = 0
		self.k += degree
		self.lockedL = True


	def adjustB(self,degree):
		self.b += (self.l * degree)
		self.k += degree

		self.lockedL = True

	def adjustL(self, degree):
		forestRange = self.b - self.a 
		incr = -1

		if degree < 0:
			incr = 1

		for i in range(degree):
			if self.l > 1:
				self.l += incr
				while self.l > 0  and self.l < forestRange and (forestRange % self.l) !=0:
					self.l += incr

		self.k = forestRange//self.l 



		#create node and perform avl insert
		#increment tree size
		#check balance of local tree
	def insertInTree(self, index, key):
		node = Node(key)
		self.treeSizes[index] += 1
		self.incrementForestSize() 

		root = self.directory[index]
		node.left = root
		if root is not None:
			root.parent = node
		self.directory[index] = node 

		if self.treeSizes[index] > self.t + 1:
			self.balance()


	def validateNodes(self, index):
		return self.traverseTree(self.directory[index], index)

	def traverseTree(self, node, actualIndex):
		if node is not None:
			self.traverseTree(node.left,actualIndex)
			print("TRAV:",node.data)
			yield node.data

		

	

	def deleteNode(self, root, key, index):
		node = self.directory[index]

		if node.data == key:
			self.directory[index] = node.left
			if node.left is not None:
				node.left.parent = None
		else:
			while node.data != key:
				node = node.left

			node.parent.left = node.left
			if node.left is not None:
				node.left.parent = node.parent


		self.decrementTreeSize(index)
		self.decrementForestSize()




	def printForest(self):
		print(self.a,"-->",self.b)
		print("n:",self.n)
		print("k:", self.k)
		print("t:",self.t)
		print("l:",self.l)
		print("Forest:")
		for i in range(self.k+2):
			print(i,":",end='')
			r = self.directory[i]
			while r is not None:
				print(r.data,"",end='')
				r = r.left
			print("")


bsf = BalancedSearchForest()
for i in range(100):
	if i%5 == 0:
		bsf.insert(i)
		bsf.printForest()
		print("~~~~~~~~~~~~~~~~~~~~~~~~")

