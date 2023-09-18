"""
This is an environment to build out Object-Oriented Programming
"""
class Employee:

    raise_amount = 1.05
    def __init__(self, first, last, job, salary):
        self.first = first
        self.last = last
        self.job = job
        self.salary = salary
        self.email = f'{first}.{last}@email.com'

    @property
    def fullname(self) -> str:
        return f'{self.first} {self.last}'

    @fullname.setter
    def fullname(self, name):
        first, last = name.split(" ")
        self.first = first
        self.last = last

    def apply_raise(self) -> int:
        self.salary = int(self.salary * self.raise_amount)
        return self.salary

    # classmethod overrides the class global variable (set at the top)
    @classmethod
    def set_raise_amt(cls, amount)-> int:
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, string):
        first, last, job, salary = string.split("-")
        return cls(first, last, job, salary)

    def __repr__(self) -> str:
        class_name = type(self).__name__
        return f'{class_name}({self.first} {self.last}, {self.job}, {self.salary})'

    def __str__(self) -> str:
        return f"The Employee's name is {self.first} {self.last} and their job title is {self.job}"

class Developer(Employee):
    raise_amount = float(1.10)

    def __init__(self, first: str, last: str, job: str, salary:float, prog_lang:str):
        super().__init__(first, last, job, salary)
        self.prog_lang = prog_lang

class Manager(Employee):
    def __init__(self, first: str, last: str, job: str, salary: float, employees: list[str]|None = None):
        super().__init__(first, last, job, salary)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, employee: Employee):
        if employee not in self.employees:
            return self.employees.append(employee)
        else:
            print('Already managing')

    def remove_emp(self, employee: Employee):
        if employee in self.employees:
            return self.employees.remove(employee)
        else:
            print('Not currently managed')

    def print_emps(self):
        for emp in self.employees:
            print(emp.fullname)

emp_1 = Employee('Bob', 'Biela', 'Data Engineer', 100000)
print(repr(emp_1))

print(emp_1.salary)
print(emp_1.apply_raise())

dev_1 = Developer('Dominic','Biela','Data Engineer',500000,'Python')

print(dev_1.email)

man_1 = Manager('Jermey','Brown','Manager',550000)
man_1.add_emp(dev_1)
man_1.add_emp(emp_1)
man_1.add_emp(dev_1)
print(man_1.employees)
man_1.remove_emp('Dominic Biela')
print(man_1.print_emps())