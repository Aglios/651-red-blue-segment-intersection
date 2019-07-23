import clipping as cp
import matplotlib.pyplot as plt

testsB=[]

def flipX(redSq,px,py,qx,qy,intsec):
    segs=cp.AllSegments(intsec)
    segs.addRedSq(redSq)
    segs.addBlue(px,py,qx,qy)
    segs.addBlue(-px,py,-qx,qy)
    testsB.append(segs)
    return segs

def flipY(redSq,px,py,qx,qy,intsec):
    segs=cp.AllSegments(intsec)
    segs.addRedSq(redSq)
    segs.addBlue(px,py,qx,qy)
    segs.addBlue(px,-py,qx,-qy)
    testsB.append(segs)
    return segs

def flipXY(redSq,px,py,qx,qy,intsec):
    segs=cp.AllSegments(intsec)
    segs.addRedSq(redSq)
    segs.addBlue(px,py,qx,qy)
    segs.addBlue(py,px,qy,qx)
    testsB.append(segs)
    return segs

def flipNegXY(redSq,px,py,qx,qy,intsec):
    segs=cp.AllSegments(intsec)
    segs.addRedSq(redSq)
    segs.addBlue(px,py,qx,qy)
    segs.addBlue(-py,-px,-qy,-qx)
    testsB.append(segs)
    return segs


B0=flipX(4,3,3,4,4,0)
B1=flipY(4,3,3,4,4,0)
B2=flipNegXY(4,4,4,5,5,0)
B3=flipY(4,0,4,0,5,0)
B4=flipX(4,-3,0,-4,0,0)
B5=flipXY(4,-6,-1,1,5,4)
B6=flipXY(4,-2,1,-1,3,0)
B7=flipNegXY(4,1,3,5,6,2)
B8=flipX(4,3,3,7,0,2)
B9=flipX(4,1,-1,2,2,0)
B10=flipNegXY(4,-5,-1,3,-6,4)
B11=flipXY(4,-5,-3,-3,-3,2)
B12=flipXY(4,-4,-4,-2,-6,0)
B13=flipX(4,1,-3,2,-2,0)
B14=flipXY(4,4,-4,5,-2,0)
B15=flipY(4,-5,-3,5,-3,4)