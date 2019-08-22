import boolop as bo
import matplotlib.pyplot as plt
'''
def plotList(list):
    for i in range(len(list)):
        list[i].plot()
    plt.show()

b1=cp.Bundle.fromCoord(-6,0,-2,0,0)
b2=cp.Bundle.fromCoord(-5,2,-2,5,0)
b3=cp.Bundle.fromCoord(-5,1,5,1,0)

rbt=cp.Tree(cp.Node(b1))
rbt.insert(b2)
rbt.insert(b3)

plotList(rbt.inorder())

rbt.delete(b1)

plotList(rbt.inorder())

a=cp.Segment.fromCoord(2,5,5,2,0)

b2.insert(a)

plotList(rbt.inorder())
'''
pts=[bo.Point(0,0),bo.Point(0,4),bo.Point(1,0),bo.Point(1,2),bo.Point(3,2),bo.Point(3,4)]

cs=bo.ConvSweep(pts[0])
for i in range(len(pts)-1):
    cs.addPt(pts[i+1],1)
    cs.plot()
    plt.show()