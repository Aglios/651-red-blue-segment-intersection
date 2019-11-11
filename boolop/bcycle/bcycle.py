#data structure for bcycle, stores bcycles below, above, and polygon
'''
required methods:
adds point to polygon
check if polygon is finished
merge bcs
set above bc and if sibling or child
add toBel(sibling or child)
visit subtree wrt to sibling below

Tools needed:
stabbing line to check sibling or child
hashmap from segments to bcs
'''


class BCycle:
	def __init__(self,flag):
		self.poly=[flag.pt]

#above/below relationship
		self.siblBel=[]
		self.childBel=[]
		self.above=None

#for nesting relationship
		self.parent=None
		self.children=None



#adds flag point to polygon
#input: terminal flag
#output: true if flag point completes the polygon, false otherwise
	def addToPoly(self,flag):
		assert(flag.type==1)
		if self.poly[0]==flag.seg.p:
			self.poly.insert(0,flag.pt)
		elif self.poly[-1]==flag.seg.p:
			self.poly.append(flag.pt)
		else:
			raise Error

		if self.poly[0]==self.poly[-1] and len(self.poly)>1:
			return True
		else:
			return False

#determine the bc of the polygon above flag and add self to bc appropriately
#set self.above to forementioned bc
#input: terminal flag that ends polygon
#output:
	def setAbove(self,flag):
		segNode=pbline.findFlag(flag)[1] #function that finds the node of segment above flag
		A=BC(segNode.seg)
		self.above=A

		number=self.stabNum(segNode,A)
		if (number%2==0):
			A.addToSibl(self)
		else:
			A.addToChild(self)


#input: bcycle below
#output:
	def addToSibl(self,bcycle):
		self.siblBel.append(bcycle)

#input: bcycle below
#output:
	def addToChild(self,bcycle):
		self.childBel.append(bcycle)

#compute stabbing number
#input: node of segment in pbline directly above terminal flag that finishes poly, boundary cycle A
#output: number of times pbline intersects polygon A going upwards
	def stabNum(self,segNode,A):
		number=0
		assert(BC(segNode.seg)==A) #BC maps segments to bcs
		while (segNode!=None):
			number+=(BC(segNode.seg)==A)
			segNode=segNode.abv
		return number

#traversal of tree wrt sibling below
#input: storage
#output:
	def traverse(storage)
