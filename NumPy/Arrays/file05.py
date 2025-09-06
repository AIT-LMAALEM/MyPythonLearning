import numpy as np 

# Slicing => [Start : End : Steps]   Not Encludinf End
a=np.array(["A","B","C","D","E","F"])
print(a[2])
print(a[1:3])
print(a[2:4])
print(a[::-1])

b=np.array([["A","B","C"],["D","E","F"],["G","H","I"],["K","L","M"],["N","S","T"]])

print(b[0])
print(b[:3])
print(b[:3,:2])
print(b[::-1])
print(b[::-1,:2])


