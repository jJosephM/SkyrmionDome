from difflib import Differ
from sympy import *
import numpy as np
a = symbols('a')

# b = diff(cos(a), a)
# print(b)

xvalues = [6,7,12,15,17,20,22,25,27,30,33]
yvalues = [16,32,64,80,96,112,128,160,176,184,192]
xsquared = []
for i in xvalues:
    xsquared.append(a*i*i)
xarray = np.array(xsquared)
yarray = np.array(yvalues)
resid = np.subtract(xarray, yarray)
resid = np.square(resid)
derivation = diff(resid,a)
print(derivation)
sum = 0
for i in derivation:
    sum += i
print(sum)
result = solveset(sum,a)
print(result)

