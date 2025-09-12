# ---------------------------------
# Compare Data Location And Type
# ---------------------------------

import numpy as np

my_list=[1,2,3,4,5,6,7,8,9]
my_array=np.array(my_list)

print(id(my_list[0]))
print(id(my_list[1]))

print(id(my_array[0]))
print(id(my_array[1]))

my_list_of_data=[1,2,"A",True,4.4]
my_array_of_data=np.array(my_list_of_data)


print(my_list_of_data)
print(my_array_of_data)    #=> ['1' '2' 'A' 'True' '4.4']

print(type(my_list_of_data[0]))    # int
print(type(my_array_of_data[0]))   # type numpy.str__

