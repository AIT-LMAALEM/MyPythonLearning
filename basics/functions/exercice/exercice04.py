# default parameters

def say_hello(name="unknown",age="unknown",country="unknown"):
    print(f"hello {name} your age is {age} and your country is {country}")

say_hello("mahmoud",15,"egypt")
say_hello("mahmoud",15)
say_hello("mahmoud")
say_hello()


# packing, unpacking arguments **kwargs
def show_skills(*skills):
    for skill in skills:
        print(f"{skill}")
show_skills("html","css","js")



myskills={
   "html":"80%",
   "Css":"70%",
   "js":"75%"
}
mytuple=("html","css","js")

def show_skills(**skills):
    for skill,value in skills.items():
        print(f"{skill} => {value}")

show_skills(html="80%",Css="70%",js="75%")
show_skills(**myskills)



def show_skills(name,*skills,**skillWithProgres):
    for skill in skills:
        print(f"{skill}")
    print("skills with progres:")
    for skill,value in skillWithProgres.items():
        print(f"{skill} :{value}")
show_skills("ibrahim","html","css","js",**myskills)
show_skills("ibrahim",*mytuple,Python="55%")




