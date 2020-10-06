from .user import User


class Member(User):
    def __init__(self, username, email):
        super().__init__(username, email)

    @staticmethod
    def members():
        return ['member1', 'member2', 'member3']

    def work(self):
        return 'work do member'
