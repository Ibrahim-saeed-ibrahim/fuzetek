from user import User  # Importing User class
from admin import Admin  # Importing Admin class

class ChatApp:
    def __init__(self):
        self.users=[]

    def register_user(self, username, role="regular"):
         for i in range (len(self.users_list)):
            if self.username[i] == self.users_list:
                print (" invalid change your username")
            if self.role== "regular":
               self.user.append(username)
               return User(username)
            elif self.role == "admin":
                 self.user.append(username)
                 return Admin(username)
           
       

       


    def find_user(self, username):
        for i in range (len(self.users_list)):
            if self.username[i] == self.users_list:
               print (" idoesnot exsist")
  