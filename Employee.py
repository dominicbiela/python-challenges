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

    def __repr__(self) -> str:
        class_name = type(self).__name__
        return f'{class_name}({self.first} {self.last}, {self.job}, {self.salary})'

    def __str__(self) -> str:
        return f"The Employee's name is {self.first} {self.last} and their job title is {self.job}"


class Developer(Employee):

    def __init__(self):
        super().__init__()

    def salary_bonus(self) -> int:
        pass


emp_1 = Employee('Bob', 'Biela', 'Data Engineer', 100000)
print(repr(emp_1))

print(emp_1.salary)
print(emp_1.apply_raise())
