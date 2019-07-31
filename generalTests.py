import boolop as bo
import matplotlib.pyplot as plt

E1=bo.AllSegments(7)
E1.addPoly([(-4,-3),(-4,2),(4,7)],0)
E1.addPoly([(2,-1),(2,1),(3,2),(3,1),(4,0)],0)
E1.addPoly([(2,-6),(4,-5),(4,-6)],0)
E1.addPoly([(-6,-5),(-5,-5),(-5,-6),(-6,-6)],0)


E1.addPoly([(-5,1),(-4,4),(-3,2)],1)
E1.addPoly([(-2,2),(-2,4),(4,3),(4,2)],1)
E1.addPoly([(2,-1),(2,1),(3,1),(3,-1)],1)
E1.addPoly([(2,-6),(6,-4),(6,-6)],1)
E1.addPoly([(-6,-5),(-4,-5),(-4,-7),(-6,-7)],1)

E1.plot()
plt.show()


print('matches expected intersection:',E1.sweep())