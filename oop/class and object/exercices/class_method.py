# instance methods: take self parameter which point to instance created from class
#class methods :marked with @classmethod / it take cls parameter not self to point to the class

# static methods:it takes no parameters
class Members:

    not_allowed_list=["hell","shift","baloot"]
    user_num=0

    @classmethod
    def show_users_count(cls):
        print(f"we have {Members.user_num} member")
    @staticmethod
    def say_hello():
        print("hello")

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
    


Members.show_users_count()
Members.say_hello()

