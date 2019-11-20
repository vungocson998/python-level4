# Create first class in python
# def __init__(self):
# Class variables, instance variables

class Employee:
    company = "Home"
    def __init__(self, name, email):
        self.name = name
        self.email = email
    def printName(self):
        return(self.name)
    def printEmail(self):
        return(self.email)
# Instance variables
emp_1 = Employee("TED", "TED.com")
emp_2 = Employee("Duong", "Duong.com")


print(type(emp_1))
print(emp_1.printName())
#Same result
print(Employee.printName(emp_1))

print(Employee.company)
print(emp_1.company)