import clipping as cp
import matplotlib.pyplot as plt

a=cp.AllSegments()
a.addRedSq(2)
a.addBlue(-3,0,0,3)
#a.addBlue(0,1,3,4)
#a.addBlue(0,0,3,0)
#a.addBlue(1,0,4,4)
#a.plot()
a.sortFlags()
a.sweep()