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