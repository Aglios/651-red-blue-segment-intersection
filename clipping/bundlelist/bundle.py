from ..tree.tree import Tree
import matplotlib.pyplot as plt
#SM:reworked bundle class: self.tree, abv, bel are all pointers. color is constant
#all the abv bel changes are done in BundleList
class Bundle:
    def __init__(self,tree=None, bel=None,abv=None):
        self.tree=tree
        if tree == None:
          self.color = None
        else:
          self.color = tree.root.seg.color
        self.bel=bel
        self.abv=abv
        
    #class method to create a single segment bundle
    def fromSeg(seg, bel=None, abv=None):
        return Bundle(Tree.fromSeg(seg), bel, abv)

    def fromCoord(px,py,qx,qy,color,bel=None,abv=None):
        return Bundle(Tree.fromCoord(px,py,qx,qy,color),bel,abv)
    
    #set fields to None
    #JSS: I don't know if we need to do this or if python will do it for us, but this is really the __del__ function.
    def setNone(self):
        self.tree=None
        self.abv=None
        self.bel=None
        self.color=None
        return self

    #set fields to other's fields
    def setTo(self,other):
        self.tree=other.tree
        self.abv=other.abv
        self.bel=other.bel
        self.color=other.color
        return self
    
    def __flagTestHelper(self,node,flag):
        cmp=flag.cmpSeg(node.seg)
        if cmp<0:
            if node.left==None:
                return [node,-1]
            return self.__flagTestHelper(node.left,flag)
        elif cmp>0:
            if node.right==None:
                return [node,1]
            return self.__flagTestHelper(node.right,flag)
        else:
            return [node,0]
    
    #input: flag
    #output: a node directly above or below it with indication (0:flag on seg, -1:flag below, 1:flag above)
    def flagTest(self,flag):
        return self.__flagTestHelper(self.tree.root,flag)
    
    def split(self,seg):
        return self.tree.splitTree(seg)
    
    #input:other bundle
    #output:join other bundle into self, delete other bundle
    def join(self,other):
        self.tree=self.tree.joinTrees(other.tree)
        other.setNone()
        return self

    #input: segment
    #output: delete segment from bundle
    def delete(self,seg):
        self.tree=self.tree.delete(seg)
        if self.tree.root==None:
            self.setNone()
        return self
    
    def pairs(self,other,intsec):
        A=self.tree.inorder()
        B=other.tree.inorder()
        for i in range(len(A)):
            for j in range(len(B)):
                intsec.append((A[i],B[j]))
        return intsec


    def insert(self,seg):
        assert seg.color==self.color
        return self.tree.insert(seg)
    def contains(self,seg):
        return self.tree.contains(seg)
    def max(self):
        return self.tree.max
    def min(self):
        return self.tree.min
    def isEmpty(self):
        return self.tree==None
    def size(self):
        return self.tree.size
    
    def plot(self):
        l=self.tree.inorder()
        for i in range(len(l)-1,-1,-1):
            l[i].prt()
            l[i].plot()
        print(' ')
        plt.axis('equal')
        
    def prt(self):
        l=self.tree.inorder()
        for i in range(len(l)-1,-1,-1):
            l[i].prt()
        print(' ')
        
    def cmp(self,other):
        if self.bel!=None and self.bel.color==other.color:
            if self.bel.max()<other.max():
                return -1
            return 1
        elif self.abv!=None and self.abv.color==other.color:
            if self.abv.max()<=other.max():
                return -1
            return 1
        elif other.abv!=None and self.color==other.abv.color:
            if self.max()<other.abv.max():
                return -1
            return 1
        elif other.bel!=None and self.color==other.bel.color:
            if self.max()<=other.bel.max():
                return -1
            return 1
        else:
            raise NameError("bundles not comparable")
    
    #only for comparing bundles of opposite color, ordering determined by the ordering in the bundleList
    def __lt__(self,other):
        return self.cmp(other)<0
        
    def __gt__(self,other):
        return self.cmp(other)>0