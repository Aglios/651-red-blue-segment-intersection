import boolop as bo
from testsA import testsA
from testsB import testsB
from testsC import testsC
from testsD import testsD



for i in range(len(testsA)):
    if not testsA[i].sweep():
        print('test',i,"does not match expected intersection")
print('test complete')

for i in range(len(testsB)):
    if not testsB[i].sweep():
        print('test',i,"does not match expected intersection")
print('test complete')

for i in range(len(testsC)):
    if not testsC[i].sweep():
        print('test',i,"does not match expected intersection")
print('test complete')

for i in range(len(testsD)):
    if not testsD[i].sweep():
        print('test',i,"does not match expected intersection")
print('test complete')

