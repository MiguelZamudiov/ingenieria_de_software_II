from logger import Logger


class UserService:

    def __init__(self):
        self.logger = Logger()

    def create_user(self, name):
        self.logger.log(f"Usuario creado: {name}")