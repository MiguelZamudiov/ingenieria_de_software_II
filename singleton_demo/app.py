from user_service import UserService
from logger import Logger


class App:

    def __init__(self):
        self.user_service = UserService()

    def run(self):

        self.user_service.create_user("Miguel")
        self.user_service.create_user("Ana")

        logger1 = Logger()
        logger2 = Logger()

        print(logger1 == logger2)