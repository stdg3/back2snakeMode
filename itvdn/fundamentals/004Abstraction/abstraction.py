class Core:
    def __init__(self) -> None:
        self._types = {
            "A": 100,
            "B": 200
        }

    def get_salary(self, class_name):
        return self._types.get(class_name, 0)


class AccountiongInterface:
    def __init__(self,db) -> None:
        self.core = Core()
        self.database = db
    
    def get_salary(self, name):
        class_of_employee = self.database.get(name)
        salary = self.core.get_salary(class_of_employee)
        return salary
    

local_db = {"Mike": "B", "John": "A"}

interface = AccountiongInterface(local_db)
print(f"John salary:{interface.get_salary(name='John')}")
