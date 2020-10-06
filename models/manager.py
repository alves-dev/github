from .user import User


class Manager(User):
    def __init__(self, username, email):
        super().__init__(username, email)

    def work(self):
        return 'work do manager'

    @staticmethod
    def manger_func():
        return 'alguma função do manager'
