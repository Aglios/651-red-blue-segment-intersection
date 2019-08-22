from .basic.segment import Segment
from .basic.flag import Flag
from .bundlelist.bundlelist import BundleList

import matplotlib.pyplot as plt

#for building segments
class AllSegments:
    def __init__(self,expectedInt):
        self.red=[]
        self.blue=[]
        self.flags=[]
        self.intList=[]
        self.totalInt=0
        self.eint=expectedInt
        self.max=0

    def clear(self):
        self.red=[]
        self.blue=[]
        self.flags=[]
        self.intList=[]
        self.totalInt=0
        self.max=0

    #adding segments 
    def addRed(self,px,py,qx,qy):
        m=max(abs(px),abs(py),abs(qx),abs(qy))
        if m>self.max:
            self.max=m
        self.red.append(Segment.fromCoord(px,py,qx,qy,0))

    def addBlue(self,px,py,qx,qy):
        m=max(abs(px),abs(py),abs(qx),abs(qy))
        if m>self.max:
            self.max=m
        self.blue.append(Segment.fromCoord(px,py,qx,qy,1))
    
    #create square with endpts (-x,-x), (-x,x), (x,-x), (x,x)
    def addRedSq(self,x):
        self.addRed(-x,-x,-x,x)
        self.addRed(-x,-x,x,-x)
        self.addRed(x,x,x,-x)
        self.addRed(x,x,-x,x)

    #input:vertices in ccw
    #output: adds polygon
    def addPoly(self,vertices,color):
        assert len(vertices)>=3
        for i in range(len(vertices)-1):
            self.__addSeg(vertices[i],vertices[i+1],color)
        self.__addSeg(vertices[0],vertices[-1],color)

    def __addSeg(self,p,q,color):
        if color==0:
            self.addRed(p[0],p[1],q[0],q[1])
        else:
            self.addBlue(p[0],p[1],q[0],q[1])

    def partition(self,arr,low,high): 
        i = ( low-1 )         
        pivot = arr[high]      
        for j in range(low , high):      
            if   arr[j].cmp(pivot)<=0:             
                i = i+1 
                arr[i],arr[j] = arr[j],arr[i] 
        arr[i+1],arr[high] = arr[high],arr[i+1] 
        return ( i+1 ) 

    def quickSort(self,arr,low,high): 
        if low < high: 
            pi = self.partition(arr,low,high) 
            self.quickSort(arr, low, pi-1) 
            self.quickSort(arr, pi+1, high)

    def sort(self,arr):
        self.quickSort(arr,0,len(arr)-1)

    #return the sorted list of flags
    def sortFlags(self):
        self.flags=[]
        for i in range(len(self.red)):
            self.flags.append(Flag(self.red[i],self.red[i].p))
            self.flags.append(Flag(self.red[i],self.red[i].q))
        for i in range(len(self.blue)):
            self.flags.append(Flag(self.blue[i],self.blue[i].p))
            self.flags.append(Flag(self.blue[i],self.blue[i].q))
        self.sort(self.flags)
    
    #plot all the segments
    def plot(self):
        for i in range(len(self.red)):
            self.red[i].plot()
        for i in range(len(self.blue)):
            self.blue[i].plot()
        plt.axis('equal')
        plt.show()

    def prtIntsec(self,index=-1):
        intsec=self.intList[index]
        for i in range(len(intsec)):
            intsec[i][0].prt()
            intsec[i][1].prt()
            print(' ')

    #sweeps the ordered flags
    def sweep(self):
        bl=BundleList(self.max+1)
        self.sortFlags()
        for i in range(len(self.flags)):
            intsec=bl.procFlag(self.flags[i])
            self.totalInt+=len(intsec)
#            self.intList.append(intsec)
#            self.prtIntsec()
#            bl.plot()
#            plt.show()
        if self.totalInt==self.eint:
            return True
        return False

    def sweepDetails(self):
        bl=BundleList(self.max+1)
        self.sortFlags()
        for i in range(len(self.flags)):
            bl.procFlag(self.flags[i])
            print('bundlelist')
            bl.plot()
            plt.show()