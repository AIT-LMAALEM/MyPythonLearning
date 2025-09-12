# --------- Compare Performance And Memory Use
#-----------------------------------------------------
# Performance 
# Memory Use

import numpy as np
import time


elements=150000
my_list1= range(elements)
my_list2= range(elements)

my_array1=np.arange(elements)
my_array2= np.arange(elements)

list_start= time.time()
list_result = [ (n1 + n2) for n1, n2 in zip(my_list1, my_list2)]
print(f"List time :{time.time() -list_start}")

array_start= time.time()
array_result = my_array1 + my_array2
print(f"Array time :{time.time() - array_start}")



############################
my_array =np.arange(1000)
print(my_array.itemsize)
print(my_array.size)
print(f"All Bytes:{my_array.itemsize * my_array.size}")

