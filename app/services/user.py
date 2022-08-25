from app.models.user import User
class UserService(object):
    def __init__(self) -> None:
        pass
    
    def login(self, id, password):
        loginip = User(id,password)
        print(f'아이디: {loginip.id}')
        print(f'비번: {loginip.password}')
