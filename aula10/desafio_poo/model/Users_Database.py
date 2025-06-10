from model.User import User

class Users_Database:
    def __init__(self) -> None:
        self.users = []

    def add_user(self, user: User):
        self.users.append(user)

    def get_users(self) -> None:
        if len(self.users) == 0:
            print('Não há usuários registrados')
        else:
            for user in self.users:
                print(f'{user.id} | {user.name} | {user.salary} | {user.fgts:.2f} | {user.inss:.2f} | {user.salary - user.inss:.2f}')