class Worker:
    RIGHTS = 'Equals'
    SALARY_MAP = {
            'A' : 100,
            'B' : 200,
            'C' : 500
        }
    
    def __init__(self, worker_class):
        self.__salary = self.__get_salary(worker_class)

    @staticmethod
    def __get_salary(worker_class):
        return Worker.SALARY_MAP.get(worker_class, 0)
    
    # Getter
    @property
    def salary(self):
        return self.__salary

worker = Worker(worker_class='A')
print(worker.salary)

