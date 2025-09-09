import numpy as np 
# Broadcasting 

a = np.array([1,2,3])
print(a + 5)  # Sclaar broadcasting
print(a * 2)
print(a.shape)  # (3,)

b = np.array([[1,2],[3,4]])
print(b + 10)

x = np.array([1,2,3])[:,None]
print(x)   #shape (3,1)

y = np.array([1,2,3])[None,:]
print(y)  #shape (1,3) 

# ligne => colonne
A = np.array([1,4,7,9])
B = A[:,None]
print(B)
print(B.shape)
C = A[None,:]
print(C)
print(C.shape)
# matrice B (4,1) * C (1,4)
print(B*C)

