#Jimmy Vo
#Jimmyvo866@gmail.com
#CPSC 223P
#Assignment 4

import random #random module used in main
import sys

class node:
	# takes sequence of instance variables and reserves appropriate space in each instance to hold for each variable
	# space is saved due to not having attribute storage for each instances; in this case, not for the nodes
	__slots__ = {'_left', '_right', '_parent', '_key'}
	
	#each node has own variable
	def __init__(self, parent, key):
		self._parent = parent		# ex. _variable ~ private variables
		self._left = None 
		self._right = None 
		self._key = key
  
	#@property
	def getKey(self):
		return self._key
	#@key.setter
	def setKey(self, k):
		self._key = k
	#@key.deleter
	def delKey(self):
		del self._key
  
	def getRight(self):
		return self._right
		
	def setRight(self, n):
		self._right = n
		
	def delRight(self):
		del self._right
  
	def getLeft(self):
		return self._left
  
	def setLeft(self, n):
		self._left = n
  
	def delLeft(self):
		del self._left
  
	def getParent(self):
		return self._parent
  
	def setParent(self, n):
		self._parent = n
  
	def delParent(self):
		del self._parent
  
	left = property(getLeft, setLeft, delLeft)	#property function
	right = property(getRight, setRight, delRight)
	parent = property(getParent, setParent, delParent)
	key = property(getKey, setKey, delKey)

class Tree:
	__slots__ = {'_root'}
	def __init__(self):
		self._root = None
  
	def getRoot(self):
		return self._root
    
	def setRoot(self, n):
		self._root = n
    	
	def delRoot(self):
		del self._root
    
	root = property(getRoot, setRoot, delRoot )
  
	def hasKey(self, key):
		return self._find(self.root, key)
    
	def _minimum(self, r):
		n = r
		while n.left != None:
			n = n.left
		return n
  
	def _maximum(self, r):
		n = r
		while n.right( ) != None:
			n = n.right( )
		return n
  
	def _inorder(self, node):
		if node.right != None:
			ios = self._minimum(node.right)
		else:
			ios = node.parent
			tmp = node
			while ios != None and tmp == ios.right:
				tmp = ios
				ios = ios.parent
			if ios == None:
				ios = node
		return ios
  
	def _find(self, node, key):
		while node != None and node.key != key:
			if key > node.key:
				node = node.right
			else:
				node = node.left
		return node
    
    
    #gets sort key and goes down tree to put value in empty node
	def insert(self, key):
		x = self.root
		y = None
		while x != None:
			y = x
			if x.key > key:
				x = x.left
			else:
				x = x.right
		n = node(y, key)
		if y == None:
			self.root = n
		elif y.key > key:
			y.left = n
		else:
			y.right = n

	def remove(self, key):
		n = self.hasKey(key)
		if n == None:
			ret = False
		else:
			ret = True
			self._deleteNode(n)
		return ret
    
	def _transfer(self, u, v):
		if u.parent == None:
			self.root = v
		elif u == u.parent.left:
			u.parent.left = v
		else:
			u.parent.right = v
		if v != None:
			v.parent = u.parent
      
	def _deleteNode(self, n):
		if n.left == None:
			self._transfer(n, n.right)
		elif n.right == None:
			self._transfer(n, n.left)
		else:
			y = self._minimum(n.right)
			if y.parent != n:
				self._transfer(y, y.right)
				y.right = n.right
				y.right.parent = y
			self._transfer(n, y)
			y.left = n.left
			y.left.parent = y
		del n

#function to draw out tree
def writeTree(t, out):
	def _writeNull(n, nullcount, out):
		out.write('\tnull' + str(nullcount) + ' [shape=point];\n')
		out.write('\t' + str(n.key) + ' -> null' + str(nullcount) + ';\n')
  
	def _writeHelper(n, out, nullcount):
		if n.left != None:
			out.write( '\t' + str(n.key) + ' -> ' + str(n.left.key) + ';\n')
			nullcount = _writeHelper( n.left, out, nullcount)
		else:
			nullcount += 1
			_writeNull(n, nullcount, out)
		if n.right != None:
			out.write( '\t' + str(n.key) + ' -> ' + str(n.right.key) + ';\n')
			nullcount = _writeHelper(n.right, out, nullcount)
		else:
			nullcount += 1
			_writeNull(n, nullcount, out)
		return nullcount
	
	out.write('digraph BST{\n')
	out.write('\tnode [fontname="Arial"];\n')
	if t.root == None:
		out.write('\n')
	elif t.root.right == None and t.root.left == None:
		out.write('\t' + str(t.root.key) + ';\n')
	else:
		_nullCount = 0
		_writeHelper( t.root, out, _nullCount )
	out.write('}\n')

def main( ):
	if len(sys.argv) < 2:
		print('Please provide the number of keys to enter.')
		sys.exit(1) # the '1' makes it exit due to error(s)
	s = int(sys.argv[1])
	parts = int(s/3)
	t = Tree( )
	r = list(range(1,s+1)) # list from 1 to __

	print('Randomly inserting the numbers from 1 to {}.'.format(len(r)))

	
	random.shuffle(r)	#random module

	for i in r:
		print('inserted {}'.format(i))
		t.insert(i) #insert method in tree
	f = open('long.dot', 'w') #writing to dot file
	writeTree(t, f) #drawing using tree and file as parameters
	f.flush( )
	f.close( )
	
	random.shuffle(r)

	#removing some nodes to make tree smaller and more broad
	#write out to another dot file
	for n in range(1, 3):
		m = r[(n-1) * parts : (n * parts)]
		print(len(m))
		for i in m:
			print('removed {}'.format(i))
			v = t.remove(i)
			if v:
				print('\tcompleted.')
			else:
				print('\terror.')
		c = chr(n + 97)
		filename = str(c) + '.dot'
		f = open('short.dot', 'w')
		writeTree(t, f)
		f.flush( )
		f.close( )
	
if __name__ == '__main__':
	main( )
