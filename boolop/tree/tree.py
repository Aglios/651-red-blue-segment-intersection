from .node import Node
from ..basic.segment import Segment

class Tree:
    def __init__(self,node):
        self.root=node
    
    #input: value
    #output: node containing the value
    def find(self,val):
        if self.root==None:
            raise NameError("empty tree")
        node=self.__findHelper(self.root,val)
        self.__splay(node)
        assert self.root==node
        return node

    #input: root node it is searching in, value
    #output: node in tree containing the value
    def __findHelper(self,node,val):
        if val<node.val:
            if node.left==None:
                raise NameError("value not in tree")
            return self.__findHelper(node.left,val)
        elif val>node.val:
            if node.right==None:
                raise NameError("value not in tree")
            return self.__findHelper(node.right,val)
        else:
            return node

    # this is a tree operation, because it may change root, as well as a node.
    # Since rotation is used only in splay, however, it is not required to maintain the root here; splay could reset it.
    def __left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != None:
            y.left.parent = x

        y.parent = x.parent
        if x.parent == None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    # rotate right at node x
    def __right_rotate(self, x):
        y = x.left
        x.left = y.right
        if y.right != None:
            y.right.parent = x
        
        y.parent = x.parent
        if x.parent == None:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y
    
    # operations on a tree node
    # Splaying node x move x to the root of the tree
    def __splay(self, x):
        while x.parent != None:
            if x.parent.parent == None:
                if x == x.parent.left:
                    # zig rotation
                    self.__right_rotate(x.parent)
                else:
                    # zag rotation
                    self.__left_rotate(x.parent)
            elif x == x.parent.left and x.parent == x.parent.parent.left:
                # zig-zig rotation
                self.__right_rotate(x.parent.parent)
                self.__right_rotate(x.parent)
            elif x == x.parent.right and x.parent == x.parent.parent.right:
                # zag-zag rotation
                self.__left_rotate(x.parent.parent)
                self.__left_rotate(x.parent)
            elif x == x.parent.right and x.parent == x.parent.parent.left:
                # zig-zag rotation
                self.__left_rotate(x.parent)
                self.__right_rotate(x.parent)
            else:
                # zag-zig rotation
                self.__right_rotate(x.parent)
                self.__left_rotate(x.parent)
        return x # useful for testing...
      
    # insert a value into the tree
    def insert(self, val):
        y = None
        x = self.root

        while x != None:
            y = x
            if val < x.val:
                x = x.left
            else:
                x = x.right
        
        node = Node(val)
        node.parent=y
        if y == None: 
            self.root = node
        elif node.val < y.val:
            y.left = node
        else:
            y.right = node
        # splay the node
        self.__splay(node)
        assert self.root==node
        return val
    
    #SM:changed to joinNodes
    #input: node2, everything in self is smaller than the tree of node
    #output: one node that is the merge of them
    def __joinNodes(self,node2):
        if self.root==None:
            self.root=node2
            return self.root
        if node2==None:
            return self.root
        
        node=self.root.findMax()
        self.__splay(node)        #needs splaying
        assert self.root==node
        node.right=node2
        node2.parent=node
        return node
    
    #input: value of node to split at; must be in the tree. 
    #output: root nodes of two trees, everything in node1 is less than or equal to node; subtree of rightroot is greater
    #found node is placed at the root of tree, with no right child.
    def __splitNode(self,val):
        node=self.find(val)   #find the node and splay to top
        assert self.root==node
        if node.right!=None:
            rightroot=node.right
            rightroot.parent=None
        else:
            rightroot=None
        node.right=None
        return [node,rightroot]

    #input:value
    #output:self if successfully deleted
    def delete(self,val):
        [valnode,rightroot]=self.__splitNode(val)
        if valnode.left != None:
            self.root=valnode.left
            self.root.parent=None
            self.__joinNodes(rightroot)
        elif valnode.left==None and rightroot!=None: 
            self.root=rightroot
        elif valnode.left==None and rightroot==None:
            self.root=None
            return self
        return self

    # In-Order traversal
    # Left Subtree -> Node -> Right Subtree
    def inorder(self):
        list=[]
        self.__in_order_helper(self.root,list)
        return list
    
    def __in_order_helper(self, node, list):
        if node != None:
            self.__in_order_helper(node.left,list)
            list.append(node.val)
            self.__in_order_helper(node.right,list)

    def plot(self):
        list=self.inorder()
        for i in range(len(list)):
            list[i].plot()
    #Bundle oriented operations
    #input: flag
    #output: the node containing the bundle containing or directly below the flag
    def findFlag(self,flag):
        node=self.__findFlagHelper(flag,self.root)
        self.__splay(node)
        assert self.root==node
        return node.val

    def __findFlagHelper(self,flag,node):
        if flag.cmpSeg(node.val.min)<0:
            return self.__findFlagHelper(flag,node.left)
        elif node.val.abv.abv!=None and flag.cmpSeg(node.val.abv.abv.min)>=0:
            return self.__findFlagHelper(flag,node.right)
        else:
            assert flag.cmpSeg(node.val.min)>=0
            return node

#Segment oriented operations
    #class method to create a tree for a single segment 
    def fromSeg(seg):
        return Tree(Node(seg))

    def fromCoord(px,py,qx,qy,color):
        return Tree(Node(Segment.fromCoord(px,py,qx,qy,color)))
        
    def contains(self,val):
        try:
            self.find(val)
            return True
        except NameError:
            return False

    #input: other tree, self<other, no empty trees
    #output: other tree merged into self
    #SM: change other tree to have same value as self
    def joinTrees(self,other):
        self.__joinNodes(other.root)
        return self
        
    #input: value to make the split
    #output: two trees
    def splitTree(self,val):
        [node1,node2]=self.__splitNode(val)
        if node2==None:
            return [Tree(node1),None]
        return [Tree(node1),Tree(node2)]