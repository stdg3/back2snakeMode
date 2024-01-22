class User:
    def __init__(self, age, name, user_type):
        self.age = age
        self.name = name
        self.user_type = user_type
    
    def access_database(self):
        print('access granted') if self.user_type == 'superuser' else print('access denied')


class SuperUser(User):
    def __init__(self, age, name):
        super.__init__(age, name, user_type='superuser')
    

client = User(age=22, name='usr', user_type='superusers')

client.access_database()

