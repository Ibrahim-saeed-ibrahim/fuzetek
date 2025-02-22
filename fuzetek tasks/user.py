from massage import Message  # Importing Message class

class User:
    def __init__(self, username):
        self.username=username
        self.inbox=[]

    def send_message(self, recipient, content):
        m=Message(self.username , recipient.username , content)
        recipient.receive_message(m)



    def receive_message(self, message):
        self.inbox.append(message)


    def view_inbox(self):
        result = " "
        for msg in self.inbox:
            result+= msg.content
        return result    
        

