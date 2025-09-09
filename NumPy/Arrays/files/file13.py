import numpy as np 

# Boolean Mask Indexing
a = np.array([-4,-3,-2,-1,0,1,2,3,4,5,6,7,8,9,10])  
print(a%2==0)  # [True ,False, ....]
mask = (a%2==0) & (a>0)  # value True 
print(a[mask])
mask = (a%2==0) & (a<0)
print(a[mask])   # print a[True]  [-4, -2]]
mask = (a%3==0) 
print(a[mask])


arr = np.arange(1,21)
mask1 = arr%3==0
mask2 = arr%2==0
mask3 = (arr%3==0) & (arr%2==0)
print(f"Original array: {arr}")
print(f"Mltiple of 3: {arr[mask1]}")
print(f"Even Numbers: {arr[mask2]}")
print(f"Multiple of 3 And Even: {arr[mask3]}")
