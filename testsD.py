import boolop as bo
import matplotlib.pyplot as plt

testsD=[]

D0=bo.AllSegments(34)
D0.addRedSq(6)
for i in range(8):
    if i==0:
        D0.addBlue(-8,0,-5,i)
        D0.addBlue(8,0,5,i)
    else:
        D0.addBlue(-8,0,-5,i)
        D0.addBlue(8,0,5,i)
        D0.addBlue(-8,0,-5,-i)
        D0.addBlue(8,0,5,-i)

D1=bo.AllSegments(34)
D1.addRedSq(6)
for i in range(8):
    if i==0:
        D1.addBlue(0,-8,i,-5)
        D1.addBlue(0,8,i,5)
    else:
        D1.addBlue(0,-8,i,-5)
        D1.addBlue(0,8,i,5)
        D1.addBlue(0,-8,-i,-5)
        D1.addBlue(0,8,-i,5)

testsD.append(D0)
testsD.append(D1)