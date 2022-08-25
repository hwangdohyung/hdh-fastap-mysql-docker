from app.models.user import User
class UserService(object):
    def __init__(self) -> None:
        pass
    
    def login(self, id, password):
        loginip = User(id,password)
        print(f'ID: {loginip.id}',f'PASSWORD: {loginip.password}')
        # print(f'PASSWORD: {loginip.password}')
        
