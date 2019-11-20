# using __dict__() function to check contained attributes
# Use self to apply changes of class variables to single instaces
# Use class variables to count number of instances

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

# Instance variables
emp_1 = Employee("TED", "TED.com")
emp_2 = Employee("Duong", "Duong.com")
emp_3 = Employee("Hoan", "Hoan.com")

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