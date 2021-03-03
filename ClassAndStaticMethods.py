# Python Class Methods and Static Methods
import datetime


class Employee:
    raise_amount = 1.04
    num_of_emp = 0

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

        Employee.num_of_emp += 1

# Regular methods automatically pass the instance called self

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def raise_applied(self):
        self.pay = int(self.pay * Employee.raise_amount)

# Classmethods automatically pass the class as the constructor argument and we call it as cls

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str_1.split('_')
        return cls(first, last, pay)

# StaticMethods don't pass anything automatically

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


my_date = datetime.date(2016, 7, 11)
print('It is a weekday:' + str(Employee.is_workday(my_date)))

emp_str_1 = 'Avighna_Reddy_40000'
emp_str_2 = 'Shivangi_Soni_50000'
emp_str_3 = 'Rohan_Singh_30000'

new_emp_1 = Employee.from_string(emp_str_1)
print(new_emp_1.email)
print(new_emp_1.pay)

emp_1 = Employee('Reema', 'Yadav', 50000)
emp_2 = Employee('Test', 'User', 60000)