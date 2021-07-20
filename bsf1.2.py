import math
#Enums
empty_rating = -2
low_rating = 0
med_rating = 1
high_rating = 2
full_rating = 5

small_adj = 1
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
			if key < self.a:
				self.insertInTree(0,key)
			elif key >= self.b:
				self.insertInTree(2,key)
			else:
				index = self.getInnerIndex(key)
				self.insertInTree(index, key)

	def member(self, key):
		return None

	def balance(self):
		lockedL = False
		treeRatings = [0]*(self.k+2)
		for i in range(self.k+2):
			treeRatings[i] = self.treeRating(i)

		sectionSize = math.floor()


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
	def getInnerIndex(self, key):
		#pre: key is unique, valid, and within a and b 
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

		#create node and perform avl insert
		#increment tree size
		#check balance of local tree
	def insertInTree(self, index, key):
		node = Node(key)
		self.treeSizes[index] += 1
		self.incrementForestSize() 

		root = self.directory[index]
		node.left = root
		self.directory[index] = node 

		if self.treeSizes[index] > self.t:
			self.balance()

		
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

	def reassignNodes(self):
		return

bsf = BalancedSearchForest()
bsf.insert(10)
bsf.insert(20)
bsf.insert(15)
bsf.insert(5)
bsf.printForest()