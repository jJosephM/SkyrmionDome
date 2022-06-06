# from sympy import *
from turtle import shape
import numpy as np

filename = 'testOutput'
numrows = 100
rowlength = 100
numlayers = 24

xstepsize = 5.0000000000000001e-09
ystepsize = 5.0000000000000001e-09
zstepsize = 8.0000000000000005e-09

data_collected = np.loadtxt(filename, skiprows= 34, max_rows= numrows * rowlength * (numlayers+1))

slice_data = data_collected[:numrows * rowlength * numlayers]

xpartial = np.zeros(shape = ((len(slice_data)) - numrows, 3)) #partial derivatives in x
for i in range( 0, numrows):
    for j in range(0, rowlength - 1):
        xpartial[i*(rowlength-1) + j] = (slice_data[i*rowlength + j + 1] - slice_data[i*rowlength + j]) / xstepsize

ypartial = np.zeros(shape= (round((len(slice_data) / numrows)), 3)) #partial derivatives in y
for i in range(0, len(ypartial)):
    ypartial[i] = (slice_data[i + rowlength] - slice_data[i]) / ystepsize

zpartial = np.zeros(shape= (numrows * rowlength * numlayers, 3)) #partial derivatives in z
for i in range(0, len(zpartial)):
    zpartial[i] = (data_collected[i + (numrows * rowlength)] - data_collected[i]) / zstepsize

xsqr = xpartial * xpartial
ysqr = ypartial * ypartial
zsqr = zpartial * zpartial

A = xsqr.sum() + ysqr.sum()
B = zsqr.sum()
# A /= -2682682.4412454394

coefficient = (B / A) * (xstepsize / zstepsize)
print(1/coefficient)
# print(xpartial)
