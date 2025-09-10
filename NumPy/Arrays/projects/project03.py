import numpy as np 


Die1 = np.random.randint(1,7,20)
Die2 = np.random.randint(1,7,20)
sum = Die1 + Die2
print(sum)
unique1, counts1 = np.unique(Die1, return_counts=True)
unique2, counts2 = np.unique(Die2, return_counts=True)

for i,j,k,t in zip(unique1,counts1,unique2,counts2):
    print(f"{i} | {j} times And {k} | {t} times")

unique , counts = np.unique(sum, return_counts=True)
for i,j in zip(unique,counts):
    print(f"Sum {i} came out {j} times")