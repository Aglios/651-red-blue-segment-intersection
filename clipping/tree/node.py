from ..basic.segment import Segment
#warning: functions in Node class do not splay in the tree

class Node:
    def __init__(self,seg, parent=None, left=None, right=None):
        self.seg=seg
        self.parent=parent
        self.left=left
        self.right=right

    def fromCoord(px,py,qx,qy,color):
        return Node(Segment.fromCoord(px,py,qx,qy,color))

    def prt(self): # print node alone
        print('[Node:', self.seg, self.parent, self.left, self.right, ']' )
        return self
    
    #input: node
    #output: minimum node in its subtree
    def findMin(self):
        if self.left!=None:
            return self.left.findMin()
        else:
            return self

    def findMax(self):
        if self.right!=None:
            return self.right.findMax()
        else:
            return self
        
    # find the predecessor of a given node in the tree
    def predecessor(self):
        # if the left subtree is not null,
        # the predecessor is the rightmost node in the 
        # left subtree
        x=self
        if x.left != None:
            y=x.left.findMax()
            return y

        y = x.parent
        while y != None and x == y.left:
            x = y
            y = y.parent
        return y