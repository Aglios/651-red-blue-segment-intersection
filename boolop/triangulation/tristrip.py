#stores points of triangels
from ..basic.segment import Segment

class TriStrip:
    def __init__(self):
        self.triangles=[]

    
    #input: 3 points of a triangle ccw
    #output: adds it to the list of triangles
    def addTri(self,p1,p2,p3):
        self.triangles.append((p1,p2,p3))

    def plot(self):
        for i in range(len(self.triangles)):
            t=self.triangles[i]
            Segment(t[0],t[1],2).plot()
            Segment(t[1],t[2],2).plot()
            Segment(t[2],t[0],2).plot()