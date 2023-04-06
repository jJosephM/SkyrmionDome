import matplotlib.pyplot as plt
import numpy as np
from math import pi, atan

path = 'C:/Users/jmank/Desktop/oommf12b4_20200930_86_x64/oommf/SkyrmionDome/experiment/BlenderTesting/'
filename = path + 'sheddingData1'

numrows = 200   #xnodes
rowlength = 80  #ynodes
numlayers = 30  #znodes

xstepsize = 5.0000000000000001e-09
ystepsize = 5.0000000000000001e-09
zstepsize = 8.0000000000000005e-09

threshold = 0000.0

data_collected = np.loadtxt(filename) #rawdata is an array of 3D vectors


shaped_data = data_collected.reshape((numrows, rowlength, numlayers, 3)) #tensor with indices meaning positions x, y, z with a vector at each point

# for i, val in enumerate(range(3237,len(shaped_data))):
#     print(shaped_data[val,2])
#     print(val)
#     break

# print(shaped_data[0,0,0,2])

#now populate the blender scene with arrows at the points that aren't zero

num = 0
for i in range(0,numrows):
    for j in range(0,rowlength):
        for k in range(0,numlayers):
            if (shaped_data[i,j,k,2]) < threshold and (shaped_data[i,j,k,2]) > -30000.0:
                # print (i, j, k)
                # x = atan(shaped_data[i,j,k,2]/shaped_data[i,j,k,1])*(180.0/pi)
                # print(x)
                num += 1
print(num)

# print(shaped_data[1,68,0])
# print(shaped_data[1,68,0,2]/shaped_data[1,68,0,1]*(180.0/pi))
# print(atan(13/-23)*(180.0/pi))



# data = np.arange(0,90)
# data = data.reshape(30,3)
# print(data)
# # print(data[3])
# data = data.reshape(2,3,5,3)
# # print(data)
# for i in range(0,2):
#     for j in range(0,2):
#         for k in range(0,5):
#             print(data[i,j,k],k,j,i)