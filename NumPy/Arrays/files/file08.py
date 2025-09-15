# Array Shape & ReShape
#  Shape returns A tuple contains The Number  of Elements in Each Dimension

import numpy as np 

a= np.array([1,3,2,5,7,5,8,6])
print(a.ndim)
print(a.shape) # (8,)

b= np.array([[1,4],[2,7],[8,9]])
print(b.ndim)
print(b.shape) # (3,2)
print(f" ligne :{b[0]}")
print(f" colonne :{b[1]}")

d= np.array([[[1,4],[2,7],[8,9]],[[1,4],[4,7],[7,8]]])
print(d.ndim)
print(d.shape)  # (2,3,2)
print("~"*39)
# Reshepe 

c=  np.array([1,3,2,5,7,5,8,6,4,9,1,2])
print(c.reshape(4,3))  # [[1 3 2] [5 7 5] [8 6 4] [9 1 2]]
print(c.reshape(2,6))  # [[1 3 2 5 7 5] [8 6 4 9 1 2]]
print(c.reshape(6,2))  # [[1 3] [2 5] [7 5] [8 6] [4 9] [1 2]]
print(c.reshape(2,3,2)) # [[[1 3] [2 5] [7 5]] [[8 6] [4 9] [1 2]]]

