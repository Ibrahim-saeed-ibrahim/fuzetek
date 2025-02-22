from user import User  # Importing User class

class Admin(User):
    def __init__(self, username, users_list):
        self.username=username
        self.users_list=users_list
        
        

    def delete_message(self, user, message):
        if message in user.inbox:
              user.inbox.remove(message)
              




    def delete_user(self, chat_app, user):
        if user.username in chat_app.users:
            chat_app.users.remove(user.username)
        



