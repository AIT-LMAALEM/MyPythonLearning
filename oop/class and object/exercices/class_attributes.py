# Class attributes defined outside the constructor  
class Members:

    not_allowed_list=["hell","shift","baloot"]
    user_num=0

    def __init__(self,first_name,last_name,age):
        self.first_name=first_name
        self.last_name=last_name
        self.age=age
        Members.user_num+=1
    
    def name(self):
        if self.first_name in Members.not_allowed_list:
            print("invalide name!")
        else :
            return f" {self.first_name} {self.last_name}"
        
    def delet_user(self):

        Members.user_num-=1
        return f"user {self.first_name} deleted"
        
    

member1=Members("mahmod","ali",45)
member2=Members("yassine","samiri",19)

print(Members.user_num)
print(member1.name())

print(member2.delet_user())

print(member1.user_num)

