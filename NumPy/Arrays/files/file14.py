import numpy as np 
# NumPy Unique Function


a = np.array([1,2,2,2,3,5,4,4,3,9,7,6,7,8,9])
print(np.unique(a))  # return [1 2 3 4 5 6 7 8 9]
# np.unique(array, return_counts=False, return_index=False, return_inverse=False)
print("Counts:",np.unique(a, return_counts=True)[1])
print("Index",np.unique(a, return_index=True)[1])
print(np.unique(a, return_inverse=True)[1])


b = np.array([1,1,2,3,4,4,5,6,6,6,8,9,9,0,0])
unique_numbers,counts= np.unique(b, return_counts=True) # returns a tuple 

print("Unique vlues:",unique_numbers)
print("Counts:",counts)


c = np.array(["Ahmed","Sara","Ali","Mohamed","Sara","Ahmed","Ali"])
result = np.unique(c, return_counts=True)
print("Names:",result[0])
print("Counts:",result[1])


d = np.array([[1,3],[3,2]])
print(np.unique(d))  # [1 2 3]


# return_inverse

a = np.array([1,2,2,4,3,3])
print(np.unique(a, return_inverse=True)[1])  #[0 1 1 3 2 2]

