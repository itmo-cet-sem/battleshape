from .user import User


class Session:
    def __init__(self):
        self.user_list = []
        self.id = 0

    def hello(self):
        user = User()
        self.id += 1
        user.id = 1
        self.user_list.append(user)
        return self.id

    def new_session(self):
        self.user_list = []
        self.id = 0

    def to_list(self):
        message = []
        for user in self.user_list:
            key = "user_id_" + str(user.id)
            item = {
                key: user.to_dict()
            }
            message.append(item)
        return message


"""
Single instance of user session
Reinitialize if needed
"""
session = Session()
