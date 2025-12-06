
class Employee:
    """
    Base Class: Employee
    Contains: name, employee_id, salary
    """

    def __init__(self,name,employee_id,salary):
        self.name = name
        self.employee_id = employee_id
        self.salary = salary
        self.annual_compensation = 0
    
    def get_details(self):
        return f'Employee Name : {self.name} ID : {self.employee_id} Salary : {self.salary}'

    def calculate_annual_salary(self):
        return self.salary * 12


class Developer(Employee):
    
    def __init__(self, name,employee_id,salary,programing_language = None):
        super().__init__(name,employee_id,salary)
        self.programing_language = programing_language or []

    def add_language(self,language):
        self.programing_language.append(language)

    def get_details(self):
        base_details = super().get_details()
        return f"{base_details} Language {', '.join(self.programing_language)}"
    
class Manager(Employee):
    
    def __init__(self, name, employee_id, salary,team_size = 0):
        super().__init__(name, employee_id, salary)
        self.team_size = team_size

    def increase_team_count(self,count):
        self.team_size += count

    # Override 
    def calculate_annual_salary(self):
        base_salary = super().calculate_annual_salary()
        bonus = base_salary * 0.10
        return base_salary + bonus

    def get_details(self):
        base_details =  super().get_details()
        return f"{base_details} Team Size {self.team_size}"
    





dev = Developer("Pugazhendhi","S72301",40000)
dev.add_language("Python")
dev.add_language("FastAPI")

print(dev.get_details())
print(dev.calculate_annual_salary())

manager = Manager("Bhavan","S72310",50000)
manager.increase_team_count(10)

print(manager.get_details())
print(manager.calculate_annual_salary())