import numpy as np

s = np.array([[4/13],[-3/13],[-12/13]])
R = np.array([[5,-1,-3,7],[4,-4,1,-2],[9,3,0,12]])
A = np.array([[1,0,-s[0]/s[2]],[0,1,-s[1]/s[2]]])
rp = np.dot(A,R)
print(rp)