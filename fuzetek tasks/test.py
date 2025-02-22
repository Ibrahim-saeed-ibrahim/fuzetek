from chat_app import ChatApp  # Importing ChatApp class

app = ChatApp()

user1 = app.register_user("Alice")
user2 = app.register_user("Bob")
admin = app.register_user("Admin1", role="admin")

user1.send_message(user2, "Hello Bob!")
user2.send_message(user1, "Hi Alice!")

admin.delete_message(user2, user2.inbox[0])  

user1.view_inbox()
user2.view_inbox()
