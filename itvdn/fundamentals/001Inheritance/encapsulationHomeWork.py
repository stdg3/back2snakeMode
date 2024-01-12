class User:
    def __init__(self, age, name) -> None:
        self.__age = age
        self.name = name
    
    @property
    def age(self):
        return self.__age
    
    @age.setter
    def age(self, value):
        self.__age = value if self.__is_valid_age(value) else None
    
    @staticmethod
    def __is_valid_age(age):
        return age >= 0


user = User(12, 'py')
print('name:', user.name, 'age:', user.age)

user.age = 19
print('name:', user.name, 'age:', user.age)
