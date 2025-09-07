# Arithmetic & Useful Operations
#------------------------------
# Addition
# Subtraction
# Multiplication
# Dividation
#-----------------------------
# mim / max / sum ..

import numpy as np

a1= np.array([10,20,30])
a2= np.array([1,2,3])
print(a1 + a2) 
print(a1 - a2)
print(a1 * a2)
print(a1 / a2)

b1= np.array([[1,4],[3,7]])
b2= np.array([[5,4],[9,1]])

print(b1 + b2)
print(b1 - b2)
print(b1 * b2)
print(b1 / b2)

print("~"*40)

print(a1.min())
print(b1.min())
print(a2.max())
print(b2.max())

print((b1+b2).sum())

# Ravel
array1= np.array([[[1,3],[4,6]],[[3,8],[4,7]]]) # dim =3
print(array1.ravel()) # return [1 3 4 6 3 8 4 7]    dim =1

array2= np.array([[1,5],[3,8]])
print(array2.ravel())   # return [1 5 3 8]




