# Data Type And  Control Array
#-----------------------------


import numpy as np

# Show Array Data Type
array1= np.array([1,3,6])
array2= np.array([1.4,14.4,124.5])
array3= np.array(["Ahmed","Samir","Imane"])

print(array1.dtype)
print(array2.dtype)
print(array3.dtype)
print("#"*50)

#" Create Array with Specific Data Type

array4= np.array([1,3,6] ,dtype="f") # float or 'float' or 'f'
array5= np.array([1.4,14.4,124.5] ,dtype="i") # int or 'int' or 'i'
array6= np.array(["Ahmed","Samir","Imane"])

print(array4.dtype)
print(array5.dtype)
print(array6.dtype)
print("#"*50)

# Change Data Type of Existing Array

my_array =np.array([1,2,0,4,5,0,7,0])
print(my_array.dtype)
print(my_array)

my_array= my_array.astype('float')
print(my_array.dtype)
print(my_array)

my_array= my_array.astype('bool')
print(my_array.dtype)
print(my_array)






