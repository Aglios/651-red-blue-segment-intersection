from .node import Node
import sys
#warning: functions in Node class do not splay
class Tree:
    def __init__(self,treeNode,minSeg=None,maxSeg=None):
        #SM: moved color, abv, bel to Bundle,
        self.root=treeNode
        if minSeg!=None:
            self.min=minSeg
        else:
            self.min=treeNode.findMin().seg #SM: no splay

        if maxSeg!=None:
            self.max=maxSeg
        else:
            self.max=treeNode.findMax().seg
            
        self.size=len(self.inorder())
            
    #class method to create a tree for a single segment 
    def fromSeg(seg):
        return Tree(Node(seg), seg, seg)

    def fromCoord(px,py,qx,qy,color):
        return Tree(Node.fromCoord(px,py,qx,qy,color))
        
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
      
    # insert a segue into the tree
    def insert(self, seg):
        self.size+=1
        y = None
        x = self.root

        while x != None:
            y = x
            if seg < x.seg:
                x = x.left
            else:
                x = x.right
        
        node = Node(seg, y)
        if y == None: 
            self.root = node
        elif node.seg < y.seg:
            y.left = node
        else:
            y.right = node
        # splay the node
        self.__splay(node)
        
        if seg>self.max:
            self.max=seg
        if seg<self.min:
            self.min=seg
            
        assert self.root==node
        return seg
      

    #input: root node it is searching in, segue
    #output: node in tree containing the seg
    def __findHelper(self,node,seg):
        if seg<node.seg:
            if node.left==None:
                raise NameError("seg not in tree")
            return self.__findHelper(node.left,seg)
        elif seg>node.seg:
            if node.right==None:
                raise NameError("seg not in tree")
            return self.__findHelper(node.right,seg)
        else:
            return node
    
    #input:segue
    #output: node containing the seg
    def find(self,seg):
        if self.root==None:
            raise NameError("empty tree")
        node=self.__findHelper(self.root,seg)
        self.__splay(node)
        assert self.root==node
        return node
    
    def contains(self,seg):
        try:
            self.find(seg)
            return True
        except NameError:
            return False
    
    #SM: __joinNodes and __splitNode do not change self.max and self.min; The functions that use them change them
    
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
    
    #input: segue of node to split at; must be in the tree. 
    #output: root nodes of two trees, everything in node1 is less than or equal to node; subtree of rightroot is greater
    #found node is placed at the root of tree, with no right child.
    def __splitNode(self,seg):
        node=self.find(seg)   #find the node and splay to top
        assert self.root==node
        if node.right!=None:
            rightroot=node.right
            rightroot.parent=None
        else:
            rightroot=None
        node.right=None
        return [node,rightroot]

    #input:seg
    #output:self if successfully deleted
    def delete(self,seg):
        self.size-=1
        [segnode,rightroot]=self.__splitNode(seg)
        if segnode.left != None:
            self.root=segnode.left
            self.root.parent=None
            self.__joinNodes(rightroot)
        elif segnode.left==None and rightroot!=None: 
            self.root=rightroot
        elif segnode.left==None and rightroot==None:
            self.max=None
            self.min=None
            self.root=None
            return self
        
        if seg==self.max:
            self.max=self.root.findMax().seg #SM: no splays
        if seg==self.min:
            self.min=self.root.findMin().seg
        return self
        
        
    #input: other tree, self<other, no empty trees
    #output: other tree merged into self
    #SM: change other tree to have same seg as self
    def joinTrees(self,other):
        assert self.max<other.min
        self.__joinNodes(other.root)
        self.max=other.max
        self.size=self.size+other.size
        return self
        
    #input: seg to make the split
    #output: two trees
    def splitTree(self,seg):
        [node1,node2]=self.__splitNode(seg)
        if node2==None:
            return [Tree(node1,self.min,seg),None]
        return [Tree(node1,self.min,seg),Tree(node2,None,self.max)]
    
    def __in_order_helper(self, node, segList):
        if node != None:
            self.__in_order_helper(node.left,segList)
            segList.append(node.seg)
            self.__in_order_helper(node.right,segList)
    
    # In-Order traversal
    # Left Subtree -> Node -> Right Subtree
    def inorder(self):
        segList=[]
        self.__in_order_helper(self.root,segList)
        return segList
        
    def __print_helper(self, currPtr, indent, last):
            # print the tree structure on the screen
            if currPtr != None:
                sys.stdout.write(indent)
                if last:
                    sys.stdout.write("└──")
                    indent += "     "
                else:
                    sys.stdout.write("├──")
                    indent += "|    "

                print (currPtr.seg)

                self.__print_helper(currPtr.right, indent, False)
                self.__print_helper(currPtr.left, indent, True)

    # print the tree structure on the screen
    def pprint(self):
        if self.root != None:
            #if self.color == None:
              print('Tree ', self.min, self.root.seg, self.max)
            #else:
            #  print(REDBLUE[self.color], 'Tree ', self.min, self.root.seg, self.max)
        self.__print_helper(self.root, "", True)