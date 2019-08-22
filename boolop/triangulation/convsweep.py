from .tristrip import TriStrip
import matplotlib.pyplot as plt
#invariant: any two bounding segments has a convexhull linking them

'''
flag=current flag being processed
abv=segment above flag
bel=segment below flag

if orientation of abv is negative or flag is terminal:
	chull=existing convexhull for the particular bounding pair (may be a splitted hull)
else:
	chull=new convex hull with pointers to segments bounding it

startSeg=segment in the convex hull to start modifying (know which one to start (max x element or where the split happens)

gift wrap from the startSeg for the new flag

if flag is starting and is within boundary:
	pointers to newhull from the bounding segments



'''

class ConvSweep:
    class Node:
        def __init__(self,point,prv=None,nxt=None):
            self.pt=point
            self.prv=prv
            self.nxt=nxt

    def __init__(self,point):
        self.sent=ConvSweep.Node(point) #keeps points of convex hull in ccw order
        self.tristrip=TriStrip()
        self.size=1

    #input: point, ori (whether the point is in visible/hidden region on the sweepline)
                    #ori positive for ccw triangles and neg for cw
    #output: modifies the convex hull to include the point
    def addPt(self,point,ori):
        if self.size==1:
            self.sent.nxt=ConvSweep.Node(point,self.sent,self.sent)
            self.sent.prv=self.sent.nxt
            self.size+=1
            return self.sent.nxt

        #uses a modified gift-wrapping alg to modify the convex hull
        cur=self.sent
        new=None
        while new==None:
            d=self.det(cur.pt,cur.nxt.pt,point)
            if d<=0:
                nxt=cur.nxt
                new=ConvSweep.Node(point,cur,nxt)
                if d<0:
                    if ori==1:
                        self.tristrip.addTri(cur.pt,new.pt,nxt.pt)
                    else:
                        self.tristrip.addTri(cur.pt,nxt.pt,new.pt)
                cur.nxt=new
                nxt.prv=new
                self.size+=1
                break
            cur=cur.nxt
            if cur==self.sent:
                raise NameError("cannot add point")
        while new.nxt!=self.sent:
            nxt2=new.nxt.nxt
            d=self.det(new.pt,new.nxt.pt,nxt2.pt)
            if d<=0:
                if d<0:
                    if ori==1:
                        self.tristrip.addTri(new.pt,nxt2.pt,new.nxt.pt)
                    else:
                        self.tristrip.addTri(new.pt,new.nxt.pt,nxt2.pt)
                new.nxt=nxt2
                nxt2.prev=new
                self.size-=1
            else:
                return new
        return new
    
    def det(self,p,q,r):
        return (q.x-p.x)*(r.y-p.y)-(q.y-p.y)*(r.x-p.x)

    def plot(self):
        self.tristrip.plot()
        plt.axis('equal')
        plt.show()
        