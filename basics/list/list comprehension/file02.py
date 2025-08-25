fruits=["apple","banana","cherry","kiwi","mango"]
fruits_a=[]
for fruit in fruits:
    if "a" in fruit:
        fruits_a.append(fruit)
print(fruits_a)

#methode 2
fruits_a=[  fruit for fruit in fruits if "a" in fruit]
print(fruits_a)

# exe1
numbers=[1,2,3,4,5,6,7,8,9,10]
print(["even" if x%2==0 else "odd" for x in numbers])


#exe2
grades=[20,55,27,70,82,19,90]
result=["pass" if i >=50 else "fail" for i in grades]
for grad, res in zip(grades,result):
    print(f"{grad} :{res}")

#exe3
words=["on","apple","holdBack","braveMan","today"]
words_l=[word.upper() if len(word)<=3 else word.lower() for word in words]
print(words_l)


