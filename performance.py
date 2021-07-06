import random
import math
from hash import HashTable 
from bst import BinarySearchTree
from avl import AVLTree
from bplus import BPlusTree
from veb import VEBtree

sampleRange = 50
sampleBase = 10
numRounds = 7 # final test round uses sample of 10^7 
numTestSets = 1000

#parallel arrays for each structure to record work and num of ops for each op type
hashWork = [[0]*8 for i in range(8)]
hashOps = [[0]*8 for i in range(8)]

bstWork = [[0]*8 for i in range(8)]
bstOps = [[0]*8 for i in range(8)]

avlWork = [[0]*8 for i in range(8)]
avlOps = [[0]*8 for i in range(8)]

rbWork = [[0]*8 for i in range(8)]
rbOps = [[0]*8 for i in range(8)]

bplusWork = [[0]*8 for i in range(8)]
bplusOps = [[0]*8 for i in range(8)]

skipWork = [[0]*8 for i in range(8)]
skipOps = [[0]*8 for i in range(8)]

vebWork = [[0]*8 for i in range(8)]
vebOps = [[0]*8 for i in range(8)]

bsfWork = [[0]*8 for i in range(8)]
bsfOps = [[0]*8 for i in range(8)]
#first index = power of ten sample size
#Second index key:
#0 = insert
#1 = search
#2 = min
#3 = max
#4 = pred
#5 = succ
#6 = space (same num for both)
#7 = remove

#example: structure-(work/numOfOps) [sizeOfSample][opCode]


def start():
	testRound(1)
	

def testRound(roundSize):
	#generate random sample of keys
	sampleSize = sampleBase ** roundSize
	sample = random.sample(range(sampleRange),sampleSize,counts=None)

	#generate working set for operation testing. opSet size = sampleSize 
	opSubSetSize = math.floor(len(sample)/2)
	opSet = [None] * opSubSetSize

	#fill first half of working set with existing keys
	for i in range(opSubSetSize):
		opSet[i] = sample[i]

	#fill second half of working set with random keys
	opRandom = random.sample(range(sampleRange),opSubSetSize,counts=None)
	for i in range(opSubSetSize):
		opSet.append(opRandom[i])


	#begin operations

	#Order of ops:
	#	Insert full sample
	#	searches for full opset
	#	find min 
	#	find max
	#	pred ops for even indexed opset
	#	succ ops for odd indexed opset
	#	record storage space
	#	remove full sample

	#hash~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
	opCode = 0
	print("~~~~~~~~~~~~Start Hash Table performance: R", roundSize ,"~~~~~~~~~~~~~~~")
	hash = HashTable()

	#~~~~~~~~~~~~insert
	print("(1/8) Inserting ",sampleSize," keys.")
	for i in sample:
		hash.insert(i,i)

	hashWork[roundSize][opCode] += hash.getWork()
	hashOps[roundSize][opCode] += sampleSize
	print("Completed Insert- ",hashWork[roundSize][opCode]," work performed.")

	#~~~~~~~~~~~~search
	opCode += 1
	print("(2/8) Searching for ",sampleSize," keys.")
	for i in opSet:
		hash.get(i)

	hashWork[roundSize][opCode] += hash.getWork()
	hashOps[roundSize][opCode] += sampleSize
	print("Completed Searches - ",hashWork[roundSize][opCode]," work performed.")

	#~~~~~~~~~~~~min
	opCode += 1
	print("(3/8) Finding minimum for key set.")
	hash.min()

	hashWork[roundSize][opCode] += hash.getWork()
	hashOps[roundSize][opCode] += 1
	print("Completed minimum - ",hashWork[roundSize][opCode]," work performed.")

	#~~~~~~~~~~~~max
	opCode += 1
	print("(4/8) Finding maximum for key set.")
	hash.max()

	hashWork[roundSize][opCode] += hash.getWork()
	hashOps[roundSize][opCode] += 1
	print("Completed maximum - ",hashWork[roundSize][opCode]," work performed.")

	#~~~~~~~~~~~~predecessor
	opCode += 1
	print("(5/8) Performing ",opSubSetSize," predecessor operations.")
	for i in opSet:
		if (opSet.index(i) % 2) != 0:
			hash.predecessor(i)

	hashWork[roundSize][opCode] += hash.getWork()
	hashOps[roundSize][opCode] += opSubSetSize
	print("Completed predecessor operations - ",hashWork[roundSize][opCode]," work performed.")

	#~~~~~~~~~~~~successor
	opCode += 1
	print("(6/8) Performing ",opSubSetSize," successor operations.")
	for i in opSet:
		if (opSet.index(i) % 2) == 0:
			hash.successor(i)

	hashWork[roundSize][opCode] += hash.getWork()
	hashOps[roundSize][opCode] += opSubSetSize
	print("Completed successor operations - ",hashWork[roundSize][opCode]," work performed.")

	#~~~~~~~~~~~~storage
	opCode += 1
	print("(7/8) Recording storage space used.")
	hashWork[roundSize][opCode] += hash.getStorage()
	hashOps[roundSize][opCode] += hash.getStorage()

	#~~~~~~~~~~~~remove
	opCode += 1
	print("(8/8) Removing ",sampleSize," keys.")
	for i in sample:
		hash.erase(i)

	hashWork[roundSize][opCode] += hash.getWork()
	hashOps[roundSize][opCode] += sampleSize
	print("Completed removals- ",hashWork[roundSize][opCode]," work performed.")
	print("Hash Table Testing Completed \n\n")

	#bst~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
	opCode = 0
	print("~~~~~~~~~~~~Start Binary Search Tree performance: R", roundSize ,"~~~~~~~~~~~~~~~")
	bst = BinarySearchTree()

	#~~~~~~~~~~~~insert
	print("(1/8) Inserting ",sampleSize," keys.")
	for i in sample:
		bst.put(i,i)

	bstWork[roundSize][opCode] += bst.getWork()
	bstOps[roundSize][opCode] += sampleSize
	print("Completed Insert- ",bstWork[roundSize][opCode]," work performed.")

	#~~~~~~~~~~~~search
	opCode += 1
	print("(2/8) Searching for ",sampleSize," keys.")
	

	bstWork[roundSize][opCode] += bst.getWork()
	bstOps[roundSize][opCode] += sampleSize
	print("Completed Searches - ",bstWork[roundSize][opCode]," work performed.")

	#~~~~~~~~~~~~min
	opCode += 1
	print("(3/8) Finding minimum for key set.")
	bst.min()

	bstWork[roundSize][opCode] += bst.getWork()
	bstOps[roundSize][opCode] += 1
	print("Completed minimum - ",bstWork[roundSize][opCode]," work performed.")

	#~~~~~~~~~~~~max
	opCode += 1
	print("(4/8) Finding maximum for key set.")
	bst.max()

	bstWork[roundSize][opCode] += bst.getWork()
	bstOps[roundSize][opCode] += 1
	print("Completed maximum - ",bstWork[roundSize][opCode]," work performed.")

	#~~~~~~~~~~~~predecessor
	opCode += 1
	print("(5/8) Performing ",opSubSetSize," predecessor operations.")
	for i in opSet:
		if (opSet.index(i) % 2) != 0:
			bst.predecessor(i)

	bstWork[roundSize][opCode] += bst.getWork()
	bstOps[roundSize][opCode] += opSubSetSize
	print("Completed predecessor operations - ",bstWork[roundSize][opCode]," work performed.")

	#~~~~~~~~~~~~successor
	opCode += 1
	print("(6/8) Performing ",opSubSetSize," successor operations.")
	for i in opSet:
		if (opSet.index(i) % 2) == 0:
			bst.successor(i)

	bstWork[roundSize][opCode] += bst.getWork()
	bstOps[roundSize][opCode] += opSubSetSize
	print("Completed successor operations - ",bstWork[roundSize][opCode]," work performed.")

	#~~~~~~~~~~~~storage
	opCode += 1
	print("(7/8) Recording storage space used.")
	bstWork[roundSize][opCode] += bst.getStorage()
	bstOps[roundSize][opCode] += bst.getStorage()

	#~~~~~~~~~~~~remove
	opCode += 1
	print("(8/8) Removing ",sampleSize," keys.")
	

	bstWork[roundSize][opCode] += bst.getWork()
	bstOps[roundSize][opCode] += sampleSize
	print("Completed removals- ",bstWork[roundSize][opCode]," work performed.")
	print("Binary Search Tree Testing Completed \n\n")
	


	#avl~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
	opCode = 0
	print("~~~~~~~~~~~~Start AVL Tree performance: R", roundSize ,"~~~~~~~~~~~~~~~")
	avl = AVLTree()

	#~~~~~~~~~~~~insert
	print("(1/8) Inserting ",sampleSize," keys.")
	for i in sample:
		avl.insert(i)

	avlWork[roundSize][opCode] += avl.getWork()
	avlOps[roundSize][opCode] += sampleSize
	print("Completed Insert- ",avlWork[roundSize][opCode]," work performed.")

	#~~~~~~~~~~~~search
	opCode += 1
	print("(2/8) Searching for ",sampleSize," keys.")
	for i in opSet:
		avl.searchTree(i)

	avlWork[roundSize][opCode] += avl.getWork()
	avlOps[roundSize][opCode] += sampleSize
	print("Completed Searches - ",avlWork[roundSize][opCode]," work performed.")

	#~~~~~~~~~~~~min
	opCode += 1
	print("(3/8) Finding minimum for key set.")
	avl.min()

	avlWork[roundSize][opCode] += avl.getWork()
	avlOps[roundSize][opCode] += 1
	print("Completed minimum - ",avlWork[roundSize][opCode]," work performed.")

	#~~~~~~~~~~~~max
	opCode += 1
	print("(4/8) Finding maximum for key set.")
	avl.max()

	avlWork[roundSize][opCode] += avl.getWork()
	avlOps[roundSize][opCode] += 1
	print("Completed maximum - ",avlWork[roundSize][opCode]," work performed.")

	#~~~~~~~~~~~~predecessor
	opCode += 1
	print("(5/8) Performing ",opSubSetSize," predecessor operations.")
	for i in opSet:
		if (opSet.index(i) % 2) != 0:
			avl.getPredecessor(i)

	avlWork[roundSize][opCode] += avl.getWork()
	avlOps[roundSize][opCode] += opSubSetSize
	print("Completed predecessor operations - ",avlWork[roundSize][opCode]," work performed.")

	#~~~~~~~~~~~~successor
	opCode += 1
	print("(6/8) Performing ",opSubSetSize," successor operations.")
	for i in opSet:
		if (opSet.index(i) % 2) == 0:
			avl.getSuccessor(i)

	avlWork[roundSize][opCode] += avl.getWork()
	avlOps[roundSize][opCode] += opSubSetSize
	print("Completed successor operations - ",avlWork[roundSize][opCode]," work performed.")

	#~~~~~~~~~~~~storage
	opCode += 1
	print("(7/8) Recording storage space used.")
	avlWork[roundSize][opCode] += avl.getStorage()
	avlOps[roundSize][opCode] += avl.getStorage()

	#~~~~~~~~~~~~remove
	opCode += 1
	print("(8/8) Removing ",sampleSize," keys.")
	for i in sample:
		avl.remove(i)

	avlWork[roundSize][opCode] += avl.getWork()
	avlOps[roundSize][opCode] += sampleSize
	print("Completed removals- ",avlWork[roundSize][opCode]," work performed.")
	print("AVL Tree Testing Completed \n\n")

	#bplus~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
	opCode = 0
	print("~~~~~~~~~~~~Start B+ Tree performance: R", roundSize ,"~~~~~~~~~~~~~~~")
	bplus = BPlusTree(10).

	#~~~~~~~~~~~~insert
	print("(1/8) Inserting ",sampleSize," keys.")
	for i in sample:
		bplus.set(i,i)

	bplusWork[roundSize][opCode] += bplus.getWork()
	bplusOps[roundSize][opCode] += sampleSize
	print(sample)
	print("Completed Insert- ",bplusWork[roundSize][opCode]," work performed.")

	#~~~~~~~~~~~~search
	opCode += 1
	print("(2/8) Searching for ",sampleSize," keys.")
	for i in opSet:
		bplus.get(i)

	bplusWork[roundSize][opCode] += bplus.getWork()
	bplusOps[roundSize][opCode] += sampleSize
	print("Completed Searches - ",bplusWork[roundSize][opCode]," work performed.")

	#~~~~~~~~~~~~min
	opCode += 1
	print("(3/8) Finding minimum for key set.")
	bplus.min()

	bplusWork[roundSize][opCode] += bplus.getWork()
	bplusOps[roundSize][opCode] += 1
	print("Completed minimum - ",bplusWork[roundSize][opCode]," work performed.")

	#~~~~~~~~~~~~max
	opCode += 1
	print("(4/8) Finding maximum for key set.")
	bplus.max()

	bplusWork[roundSize][opCode] += bplus.getWork()
	bplusOps[roundSize][opCode] += 1
	print("Completed maximum - ",bplusWork[roundSize][opCode]," work performed.")

	#~~~~~~~~~~~~predecessor
	opCode += 1
	print("(5/8) Performing ",opSubSetSize," predecessor operations.")
	for i in opSet:
		if (opSet.index(i) % 2) != 0:
			bplus.predecessor(i)

	bplusWork[roundSize][opCode] += bplus.getWork()
	bplusOps[roundSize][opCode] += opSubSetSize
	print("Completed predecessor operations - ",bplusWork[roundSize][opCode]," work performed.")

	#~~~~~~~~~~~~successor
	opCode += 1
	print("(6/8) Performing ",opSubSetSize," successor operations.")
	for i in opSet:
		if (opSet.index(i) % 2) == 0:
			bplus.successor(i)

	bplusWork[roundSize][opCode] += bplus.getWork()
	bplusOps[roundSize][opCode] += opSubSetSize
	print("Completed successor operations - ",bplusWork[roundSize][opCode]," work performed.")

	#~~~~~~~~~~~~storage
	opCode += 1
	print("(7/8) Recording storage space used.")
	bplusWork[roundSize][opCode] += bplus.getStorage()
	bplusOps[roundSize][opCode] += bplus.getStorage()

	#~~~~~~~~~~~~remove
	opCode += 1
	print("(8/8) Removing ",sampleSize," keys.")
	for i in sample:
		bplus.remove_item(i)

	bplusWork[roundSize][opCode] += bplus.getWork()
	bplusOps[roundSize][opCode] += sampleSize
	print("Completed removals- ",bplusWork[roundSize][opCode]," work performed.")

	print("B+ Tree Testing Completed \n\n")

	#veb~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
	opCode = 0
	print("~~~~~~~~~~~~van Emde Boas Tree performance: R", roundSize ,"~~~~~~~~~~~~~~~")
	veb = VEBtree(sampleRange)

	#~~~~~~~~~~~~insert
	print("(1/8) Inserting ",sampleSize," keys.")
	for i in sample:
		veb.vebTreeInsert(i)

	vebWork[roundSize][opCode] += veb.getWork()
	vebOps[roundSize][opCode] += sampleSize
	print(sample)
	print("Completed Insert- ",vebWork[roundSize][opCode]," work performed.")

	#~~~~~~~~~~~~search
	opCode += 1
	print("(2/8) Searching for ",sampleSize," keys.")
	for i in opSet:
		veb.isMember(i)

	vebWork[roundSize][opCode] += veb.getWork()
	vebOps[roundSize][opCode] += sampleSize
	print("Completed Searches - ",vebWork[roundSize][opCode]," work performed.")

	#~~~~~~~~~~~~min
	opCode += 1
	print("(3/8) Finding minimum for key set.")
	veb.getMin()

	vebWork[roundSize][opCode] += veb.getWork()
	vebOps[roundSize][opCode] += 1
	print("Completed minimum - ",vebWork[roundSize][opCode]," work performed.")

	#~~~~~~~~~~~~max
	opCode += 1
	print("(4/8) Finding maximum for key set.")
	veb.getMax()

	vebWork[roundSize][opCode] += veb.getWork()
	vebOps[roundSize][opCode] += 1
	print("Completed maximum - ",vebWork[roundSize][opCode]," work performed.")

	#~~~~~~~~~~~~predecessor
	opCode += 1
	print("(5/8) Performing ",opSubSetSize," predecessor operations.")
	for i in opSet:
		if (opSet.index(i) % 2) != 0:
			veb.getPredecessor(i)

	vebWork[roundSize][opCode] += veb.getWork()
	vebOps[roundSize][opCode] += opSubSetSize
	print("Completed predecessor operations - ",vebWork[roundSize][opCode]," work performed.")

	#~~~~~~~~~~~~successor
	opCode += 1
	print("(6/8) Performing ",opSubSetSize," successor operations.")
	for i in opSet:
		if (opSet.index(i) % 2) == 0:
			veb.getSuccessor(i)

	vebWork[roundSize][opCode] += veb.getWork()
	vebOps[roundSize][opCode] += opSubSetSize
	print("Completed successor operations - ",vebWork[roundSize][opCode]," work performed.")

	#~~~~~~~~~~~~storage
	opCode += 1
	print("(7/8) Recording storage space used.")
	vebWork[roundSize][opCode] += veb.getStorage()
	vebOps[roundSize][opCode] += veb.getStorage()

	#~~~~~~~~~~~~remove
	opCode += 1
	print("(8/8) Removing ",sampleSize," keys.")
	for i in sample:
		veb.vebTreeDelete(i)

	vebWork[roundSize][opCode] += veb.getWork()
	vebOps[roundSize][opCode] += sampleSize
	print("Completed removals- ",vebWork[roundSize][opCode]," work performed.")

	print("van Emde Boas Tree Testing Completed \n\n")

	return
	
	



start()
