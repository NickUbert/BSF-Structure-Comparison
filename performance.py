import time
import random
import math

from avl import AVLTree
from hash import HashTable
from bplus import BPlusTree
from bst import BinarySearchTree
from veb import VEBtree
from bsf import BalancedSearchForest

avl = AVLTree()
hsh = HashTable()
bplus = BPlusTree()
bst = BinarySearchTree()
#veb = VEBtree()
bsf = BalancedSearchForest()

structures = [avl,bsf,bplus]
timeSet = []
#Generate set
keys = []
opSet = []
names = ["avl","bsf","bplus","bst","hash","veb"]

def testRound(roundSize):
	#generate random sample of keys
	sampleSize =  10000000
	sampleRange = 100000000000
	keys = random.sample(range(sampleRange),sampleSize,counts=None)

	#generate working set for operation testing. opSet size = sampleSize 
	opSubSetSize = math.floor(len(keys)/2)
	opSet = [None] * opSubSetSize

	#fill first half of working set with existing keys
	for i in range(opSubSetSize):
		opSet[i] = keys[i]

	#fill second half of working set with random keys
	opRandom = random.sample(range(sampleRange),opSubSetSize,counts=None)
	for i in range(opSubSetSize):
		opSet.append(opRandom[i])

#0: Insert 
#1: Search
#2: Minimum 
#3: Maximum
#4: Pred
#5: Succ
#6: Remove
#7: Total 
testRound(10)
strIndex = 0
for struc in structures:
	workingSet = [0,0,0,0,0,0,0,0]
	totalA = time.perf_counter()
	#Start test 

	#Insert Keys
	insertA = totalA
	for k in keys:
		struc.insert(k)
	insertB = time.perf_counter()

	#Search for keys
	memberA = time.perf_counter()
	for k in keys:
		struc.member(k)
	memberB = time.perf_counter()

	minA = time.perf_counter()
	struc.minimum()
	minB = time.perf_counter()

	maxA = time.perf_counter()
	struc.maximum()
	maxB = time.perf_counter()

	predA = time.perf_counter()
	for i in range(len(opSet)):
		if i%2 == 0:
			struc.predecessor(k)
	predB = time.perf_counter()

	sucA = time.perf_counter()
	for i in range(len(opSet)):
		if i%2 != 0:
			struc.successor(i)
	sucB = time.perf_counter()

	removeA = time.perf_counter()
	for k in keys:
		struc.remove(k)
	removeB = time.perf_counter()
	totalB = removeB

	workingSet[0] = insertB - insertA
	workingSet[1] = memberB - memberA
	workingSet[2] = minB - minA
	workingSet[3] = maxB - maxA
	workingSet[4] = predB - predA
	workingSet[5] = sucB - sucA
	workingSet[6] = removeB - removeA
	workingSet[7] = totalB - totalA
	print(names[strIndex],end=':')
	print(workingSet)
	strIndex+=1

