# Python Ojbect Oriented Programming
class Employee:
    # class variable 类变量，所有实例共享
    num_of_emps = 0
    raise_amount = 1.04

    # constructor 类的构造函数
    # self 代表类的实例，是约定俗成的写法，不是关键字
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email  = first + '.' + last + '@company.com'
        Employee.num_of_emps += 1
    
    # 类中的所有方法都必须有 self 入参
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    # class method 类方法
    # cls 代表类本身，而不是类的实例
    # 通过使用类方法，可以在不实例化类的情况下，对类变量进行修改
    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount
    
    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)
    
    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        else:
            return True
    def __repr__(self):
        return "Employee('{}', '{}', {})".format(self.first, self.last, self.pay)

    def __str__(self):
        return '{} - {}'.format(self.fullname(), self.email)
    
    def __add__(self, other):
        return self.pay + other.pay
    
    def __len__(self):
        return len(self.fullname())

# 实例化
emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'User', 60000)

emp_str_1 = 'John-Doe-70000'
emp_str_2 = 'Steve-Smith-30000'
emp_str_3 = 'Jane-Doe-90000'

print(emp_1)
print(repr(emp_1))
print(str(emp_1))
print(len(emp_1))

class Developer(Employee):
    raise_amount = 1.10

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang  = prog_lang

class Manager(Employee):
    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees  = []
        else:
            self.employees  = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print('-->', emp.fullname())

# dev_1 = Developer('Corey', 'Schafer', 50000, 'Python')
# dev_2 = Developer('Test', 'User', 60000, 'Java')

# mgr_1 = Manager('Sue', 'Smith', 90000, [dev_1])

# print(isinstance(mgr_1, Manager))