from User import User


class UserController:

    def __init__(self):
        self.users = {}

    def add_user(self, user: User):
        self.users[user.id] = user

    def remove_user(self, user: User):
        self.users.pop(user.id)

