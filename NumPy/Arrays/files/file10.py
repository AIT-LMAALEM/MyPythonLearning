import numpy as np 


a = np.zeros(10 ,dtype="int")
print(a)

b = np.ones((3,3), dtype="int")
print(b)

c = np.full((4,3),"A")  # np.full(shape, fill_value, dtype=None)
print(c)

e = np.arange(0,10,2)    # np.arange(start, stop, step, dtype=None)
print(e)

f = np.random.randint(0,10,(3,3))
print(f)

j = np.random.random((3,3))
print(j)

d = np.random.choice([1,4,7,6,9,1] , size=3, replace=True)
print(d)

d = np.random.choice([1,4,7], size=10, replace=True ,p=[0.01, 0.9, 0.09])
print(d)

h = np.eye(5 ,dtype="int")   # Matrix In
print(h)