import numpy as np

s = np.array([[4/13],[-3/13],[-12/13]])
r = np.array([[6],[2],[3]])
A = np.array([[1,0,-s[0]/s[2]],[0,1,-s[1]/s[2]]])
rp = np.dot(A,r)
print(rp)