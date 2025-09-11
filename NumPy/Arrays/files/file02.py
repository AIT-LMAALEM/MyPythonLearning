# Numpy => Create Arrays
import numpy as np

my_list=[1,2,3,4,5,6,7,8,9]
my_tuple=(1,2,3,4,5)
my_array1=np.array(my_list)
my_array2=np.array(my_tuple)

print(my_list)
print(my_array1)
print(my_array2)

print("#"*30)
# Type
print(type(my_list))
print(type(my_array1))

# Accessing Elements
print(my_list[0])
print(my_array1[0])

# 0D Array
a=np.array(10)
# 1D Array
b=np.array([10,20])
# 2D Array
c=np.array([[10,20],[1,2]])
# 3D Array
d=np.array([[[1,2],[4,5]],[[6,7],[9,12]]])

# Accessing 
print(a)
print(b[1])
print(c[0])
print(c[0][0])
print(d[1][1][1])
print(d[1,1,1])
print(d[1,1,-1])   # -1 is the last one

print("#"*30)
# Number Of Dimensions
print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)


# Customn Dimensions
vab=np.array([1,2,3],ndmin=3)

print(vab)
print(vab[0][0][1])