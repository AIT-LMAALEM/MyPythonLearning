import numpy as np

# Define two 2D arrays (matrices)
A = np.array([[1, 2],[3, 4]])

B = np.array([[5, 6],[7, 8]])

print("Matrix A:\n", A)
print("Matrix B:\n", B)

# -----------------------------------
# 1) Element-wise multiplication (*)
# Each element in A is multiplied by the corresponding element in B
C1 = A * B
print("\nElement-wise multiplication (A * B):\n", C1)


# -----------------------------------
# 2) Matrix multiplication with @ operator
# Rows of A multiplied by columns of B
C2 = A @ B
print("\nMatrix multiplication (A @ B):\n", C2)


# -----------------------------------
# 3) Matrix multiplication using np.dot()
# Same result as @ for 2D arrays
C3 = np.dot(A, B)
print("\nMatrix multiplication (np.dot(A, B)):\n", C3)


# -----------------------------------
# 4) Matrix multiplication using np.matmul()
# Same result as @ for 2D arrays
C4 = np.matmul(A, B)
print("\nMatrix multiplication (np.matmul(A, B)):\n", C4)


