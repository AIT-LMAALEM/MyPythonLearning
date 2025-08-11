# nums=[]
# for i in range(10):
#     nums.append(i)
# print(nums)

nums_l=[i for i in range(10)]
print(nums_l)

nums_m=[ i*2 for i in range(5)]
print(nums_m)

pairs=[ i for i in range(10) if i%2==0]
print(pairs)

info={
    "name":"yassine",
    "age":16,
    "email":"yassine@gmail.com",
}
tuples_list=[(key,info[key]) for key in info]
print(tuples_list)
tuples_list=[(key,info[key]) for key in info if type(info[key])==int]
print(tuples_list)


reminder=[0 if (x%2==0) else 1 for x in range(20)]
print(reminder)



names=["rachid","omar","zaineb","amine","soufiane"]
print([name[0] for name in names])