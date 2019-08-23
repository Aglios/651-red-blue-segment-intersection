from .point import Point
import matplotlib.pyplot as plt
#class for segments 
#color is 0 for red, 1 for blue, 2 for black
RBCOLOR = 'rbk'
REDBLUE = ['red','blue','black']

#invariant:  p<=q lexicographically
#ori==1 if everything to the left is inside, ori==-1 if everything to the right is inside
#
class Segment:
    def __init__(self,pointA,pointB,color):
        if pointA<pointB:
            self.p=pointA
            self.q=pointB
            self.ori=1
        else:
            self.p=pointB
            self.q=pointA
            self.ori=-1
        self.color=color
        self.chull=None
    
    def fromCoord(xp,xq,yp,yq,color):
        return Segment(Point(xp,xq),Point(yp,yq),color)
    
    def prt(self):
        print((self.p.x,self.p.y), (self.q.x,self.q.y), REDBLUE[self.color])
        return self
    
    def cmpPt(self,r):
        return (self.q.x-self.p.x)*(r.y-self.p.y)-(self.q.y-self.p.y)*(r.x-self.p.x)
    
    # JSS: does not handle colinear case or crossing cases
    def cmp(self,other):
        assert self.color==other.color  # assumes segments are the same color, asserting it
        sp=other.cmpPt(self.p)
        sq=other.cmpPt(self.q)
        if sp*sq<0:
            sp=-self.cmpPt(other.p)
            sq=-self.cmpPt(other.q)
            if sp==0:
                return sq
            return sp
        if sp==0:
            return sq
        return sp
    
  #  def cross(self,segB):
  #      return cross(self.p.x,self.p.y,self.q.x,self.q.y,segB.p.x,segB.p.y,segB.q.x,segB.q.y)
    
    def equals(self,other):
        return self.p==other.p and self.q==other.q and self.color==other.color
          
    def slope(self):
        if (self.q.x-self.p.x)==0: # JSS: IEEE 754 specifies that division by zero gives +/-Inf, so this test is not needed. 
            return float('inf') 
        else:
            return (self.q.y-self.p.y)/(self.q.x-self.p.x)

    def plot(self):
         plt.plot([self.p.x,self.q.x],[self.p.y,self.q.y],RBCOLOR[self.color])


    #ordered by aboveness (no intersections)
    #should only compare same colored segs
    def __lt__(self,other):
        return self.cmp(other)<0
    def __gt__(self,other):
        return self.cmp(other)>0
    def __eq__(self,other): # JSS: this is not an equality test but a colinearity test. Ignores color.
        if other==None:
            return False
        return self.cmp(other)==0
    def __le__(self,other):
        return self.cmp(other)<=0
    def __ge__(self,other):
        return self.cmp(other)>=0
    def __ne__(self,other):
        return not self==other