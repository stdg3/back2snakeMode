class User:
    def __init__(self, user_name):
        self.__name = user_name

    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, new_name):
        self.__name = new_name


user = User("py")
print(user.name)

user.name = 'python'
print(user.name)