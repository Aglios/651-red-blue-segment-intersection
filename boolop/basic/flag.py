from .point import Point
from .segment import Segment
#flags are made from a segment and a endpoint of the segment
#0 is for startpt, 1 is for endpt
class Flag:
    def __init__(self, segment, endpoint):
        self.seg=segment
        self.pt=endpoint
        if self.pt==self.seg.p:
            self.type=0
        elif self.pt==self.seg.q:
            self.type=1
        else:
            raise NameError('point is not an endpoint of segment')    
            
    def prt(self):
        self.pt.prt()
        self.seg.prt()
        return self
    
    def slope(self):
        return self.seg.slope()
    
    #assume: segments are broken so that no endpoint of one lies inside another.
    #        flags are compared only with segments that overlap the interval before (for start flags)
    #              or after (for terminal flags) the endpoint.  
    def cmpSeg(self,seg):
        sign=seg.cmpPt(self.pt)
        if sign<0:
            return -1
        elif sign>0:
            return 1
        else: # depends on overlap assumption.
            if self.slope()==seg.slope():
                return self.seg.color-seg.color # depends on color = 0 or 1 to give -1, 0, or 1
            else:
                slope=self.slope()-seg.slope()
                return 1 if ((slope>0) == (self.type==0)) else -1
              
#JSS: need a complete set of test cases for this cmp function
    def cmp(self, flagB):
        if self.pt<(flagB.pt):
            return -1
        elif self.pt>(flagB.pt):
            return 1
        else: # process all terminals before all starts
            if self.type != flagB.type:
                return flagB.type - self.type # -1 or 1
            else: # process segs top to bottom
                sign=1
                if self.type==1:
                    sign=-1
                slopeDiff=sign*(self.seg.slope()-flagB.seg.slope())
                if slopeDiff<0:
                    return -1
                elif slopeDiff>0:
                    return 1
                else: # process (blue above red) #  SM: process "below" first
                    return self.seg.color-flagB.seg.color

               
    def __lt__(self,other):
        return self.cmp(other)<0
    def __gt__(self,other):
        return self.cmp(other)>0
    def __eq__(self,other):
        return self.cmp(other)==0
    def __le__(self,other):
        return self.cmp(other)<=0
    def __ge__(self,other):
        return self.cmp(other)>=0
    def __ne__(self,other):
        return self.cmp(other)!=0 