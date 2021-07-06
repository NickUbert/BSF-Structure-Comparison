import sys 

class HashTable(object):
	_work_ = 0

	MINIMUM_BUCKETS = 4
	BUCKET_SIZE = 5

	def __init__(self, capacity=MINIMUM_BUCKETS*BUCKET_SIZE):
		self.size = 0
		self.threshold = capacity
		self.buckets = [[] for _ in range(capacity//self.BUCKET_SIZE)]

	def insert(self, key, value):

		bucket = self.hash(key)
		for n, element in enumerate(self.buckets[bucket]):
			if element['key'] == key:
				element['value'] = value
				self.buckets[bucket][n] = element
				return
		else:
			self.buckets[bucket].append({'key': key, 'value': value})
			self.size += 1
			if self.size == self.threshold:
				self.resize()

	def get(self, key):
		bucket = self.hash(key)
		for element in self.buckets[bucket]:
			if element['key'] == key:
				return element['value']
		
		return -1

	def erase(self, key):
		bucket = self.hash(key)
		for n, element in enumerate(self.buckets[bucket]):
			if element['key'] == key:
				del self.buckets[bucket][n]
				self.size -= 1
				return
		return -1

	def hash(self, key):
		return hash(key) % len(self.buckets)

	def contains(self, key):
		bucket = self.hash(key)
		for element in self.buckets[bucket]:
			if element['key'] == key:
				return True
		return False

	def __getitem__(self, key):
		return self.get(key)

	def __setitem__(self, key, value):
		return self.insert(key, value)

	def __len__(self):
		return self.size

	def is_empty(self):
		return self.size == 0

	def resize(self):
		capacity = self.size / self.BUCKET_SIZE * 2
		if capacity >= self.MINIMUM_BUCKETS:
			old = self.buckets
			self.buckets = [[] for _ in range(capacity)]
			for n in range(len(self.buckets)):
				self.buckets[n] = old[n]
			self.rehash()

	def rehash(self):
		for n, bucket in enumerate(self.buckets):
			for m, element in enumerate(bucket):
				new_bucket = self.hash(element['key'])
				self.buckets[new_bucket].append(element)
				del self.buckets[n][m]

	def min(self):
		if self.size == 0:
		 return -1

		v = sys.maxsize
		for n,bucket in enumerate(self.buckets):
			for m, element in enumerate(bucket):
				if self.get(element['key']) < v :
					v = self.get(element['key'])
		return v

	def max(self):
		if self.size == 0:
		 return -1

		v = -sys.maxsize
		for n,bucket in enumerate(self.buckets):
			for m, element in enumerate(bucket):
				if self.get(element['key']) > v :
					v = self.get(element['key'])
		return v

	def predecessor(self, k):
		if self.size == 0 or self.get(k) == -1:
		 return -1

		dif = sys.maxsize
		v = -1
		for n,bucket in enumerate(self.buckets):
			for m, element in enumerate(bucket):
				cur = self.get(k)-self.get(element['key'])
				if  cur > 0 and cur < dif:
					dif = cur
					v = self.get(element['key'])
		if v == -1:
			return self.get(k)

		return v

	def successor(self, k):
		if self.size == 0 or self.get(k) == -1:
		 	return -1

		dif = -sys.maxsize
		v = -1
		for n,bucket in enumerate(self.buckets):
			for m, element in enumerate(bucket):
				cur = self.get(k)-self.get(element['key'])
				if  cur < 0 and cur > dif:
					dif = cur
					v = self.get(element['key'])
					
		if v == -1:
			return self.get(k)

		return v

	def getStorage(self):
		return self.size

	# The following getter also reset the counter, so only call once
	def getWork(self):
		w = self._work_
		self._work_ = 0
		return w

	