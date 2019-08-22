import boolop as bo
import matplotlib.pyplot as plt

testsC=[]

def flips(redSq,px,py,qx,qy,intsec):
    segs=bo.AllSegments(intsec)
    segs.addRedSq(redSq)
    segs.addBlue(px,py,qx,qy)
    segs.addBlue(-px,py,-qx,qy)
    segs.addBlue(-px,-py,-qx,-qy)
    segs.addBlue(px,-py,qx,-qy)
    testsC.append(segs)
    return segs

C0=flips(4,1,3,1,5,4)
C1=flips(4,1,1,2,4,0)
C2=flips(4,1,0,3,1,0)
C3=flips(4,0,0,2,2,0)
C4=flips(4,3,2,5,3,4)
C5=flips(4,2,5,6,2,8)
C6=flips(4,4,4,6,6,0)
C7=flips(4,4,6,6,4,0)