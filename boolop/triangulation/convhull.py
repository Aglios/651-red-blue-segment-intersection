from .tristrip import TriStrip
import matplotlib.pyplot as plt
#invariant: any two bounding segments has a convexhull linking them

'''
flag=current flag being processed
abv=segment above flag
bel=segment below flag

if bel, abv are not a binding pair:
    chull=new convex (singleton) hull with pointer from abv
    return

chull=existing convexhull pointed to by abv
startPt=point with max x-coord value
new=flag point as a node
add new to chull
gift wrap cw and ccw from startPt to maintain convexity

if flag is a start flag:
    [chull1, chull2]=original chull split at new
    add pointer from flag segment to chull1
    change pointer from abv to chull2
return
'''

class ConvHull:
    #doubly linked list node used to track points on hull
    class Node:
        def __init__(self,point,prv=None,nxt=None):
            self.pt=point
            if prv==None and nxt==None:
                self.prv=self
                self.nxt=self
            else:
                self.prv=prv
                self.nxt=nxt

        def setNone(self):
            self.pt=None
            self.prv=None
            self.nxt=None
            return self


    def __init__(self,point:
        self.chull=ConvHull.Node(point) #keeps points of convex hull in ccw order
        self.startNode=self.chull #keeps the node with max x-value; changes to split point node when split happens
        self.single=True #True if chull is just a point

    #input: new point, node to insert after
    #output: insert new point as a node after node
    def insert(self,point,node):
        nxt=node.nxt
        new=ConvHull.Node(point,node,nxt)
        node.nxt=new
        nxt.prv=new
        return new

    #input: node to remove
    #output: removes node
    def remove(self,node):
        prv=node.prv
        nxt=node.nxt
        prv.nxt=nxt
        nxt.prv=prv
        node.setNone()
        return node

    #input: node to split
    #output: [chull ending at node.pt, chull starting at node.pt]
    def split(self,node):
        return
    
    #input:flag that has a point that needed to be added, tristrip that stores triangles
    #output: adds flag's point and updates fields
    def addPt(self,flag,tristrip):
        #singleton hull
        if self.single:
            self.insert(flag.pt,self.chull)
            self.startNode=self.chull.nxt
            self.single=False
            return self.chull

        #non degenerate hull

        #adds flag point
        new=self.insert(flag.pt,self.startNode)
        start1=new.nxt
        start0=self.startNode
        self.startNode=new

        #giftwrap
        self.giftWrap(start1,flag,1,tristrip)
        self.giftWrap(start0,flag,0,tristrip)
        return self.chull

    #input: starting node, flag (point) being processed, direction, tristrip
    #output: gift wrap algorithm to remove points
    def giftWrap(self,start,flag,direc,tristrip):
        cur=start
        fol=cur.nxt if direc==1 else cur.prv #direc==1 means check segments from start on ccw
        d=self.det(cur.pt,fol.pt,flag.pt)
        while (d<=0 and direc==1) or (d>=0 and direc!=1):
            tristrip.addTri(cur.pt,fol.pt,flag.pt) #add triangle to tristrip
            self.remove(cur)
            cur=fol
            fol=cur.nxt if direc==1 else cur.prv
            d=self.det(cur.pt,fol.pt,flag.pt)
        return self.chull
    
    def det(self,p,q,r):
        return (q.x-p.x)*(r.y-p.y)-(q.y-p.y)*(r.x-p.x)
        