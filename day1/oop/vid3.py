# Regular methods, class methods and static methods

# def regular_func(self, ...):

# @classmethod
# def class_method(cls, ...):
#    pass
# You can also run class method from the instances but it does not make sense
# Some example using class method


# @staticmethod
# def static_method(...):
#    pass
# static methods dont pass anything as first argument
# it almost likes normal functions
# we put it in the class to do some logical functions


class Employee:
    numb_of_emps = 0
    company = "Home"
    def __init__(self, name, email):
        self.name = name
        self.email = email
        Employee.numb_of_emps += 1
    def printName(self):
        return(self.name)
    def printEmail(self):
        return(self.email)

    @classmethod
    def from_string(cls, emp_str):
        name, email = emp_str.split('-')
        return cls(name, email)

str1 = "TED-TED.com"
str2 = "Duong-Duong.com"
str3 = "Hoan-Hoan.com"




# Instance variables
emp_1 = Employee.from_string(str1)
emp_2 = Employee.from_string(str2)
emp_3 = Employee.from_string(str3)

# List atributes
print(emp_1.__dict__)
print(emp_2.__dict__)
# More details
#print(Employee.__dict__)

# Use self to apply changes of class variables to single instaces
emp_3.company = "My wife"
print(emp_1.company)
print(emp_2.company)
print(Employee.company)
print(emp_3.company)

print(Employee.numb_of_emps)