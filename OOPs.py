# Python OOPs Concept

class Employee:
    raise_amount = 1.04
    num_of_emp = 0

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

        Employee.num_of_emp += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def raise_applied(self):
        self.pay = int(self.pay * Employee.raise_amount)


print('No of Employees before instantiating:' + str(Employee.num_of_emp))

emp_1 = Employee('Reema', 'Yadav', 50000)
emp_2 = Employee('Test', 'User', 60000)

# emp_1 = Employee()
# emp_2 = Employee()

# print(emp_2)
# print(emp_1)

# emp_1.first = 'Reema'
# emp_1.last = 'Yadav'
# emp_1.email ='Yadav.Reema@company.com'
# emp_1.pay = 50000

# emp_2.first = 'TEST'
# emp_2.last = 'user'
# emp_2.email ='TEST.user@company.com'
# emp_2.pay = 60000

print('No of Employees after instantiating:' + str(Employee.num_of_emp))
print('Emp 1 Namespace:' + str(emp_1.__dict__))
print('Emp 1 Full Name:' + emp_1.fullname())
print('Emp 1 Email:' + emp_1.email)
print("Emp 1 Initial Pay:" + str(emp_1.pay))
emp_1.raise_applied()
print("Emp 1 Pay after amount raise:" + str(emp_1.pay))
print('Emp 2 Full Name:' + emp_2.fullname())
print('EMp 2 Email:' + emp_2.email)
