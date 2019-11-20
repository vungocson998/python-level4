# Inheritance

# Method resolution order
# When you create instances of children class, python finds init() method inside this class
# If no init() function is declared, python keeps finding in parent class.
# Use help() function to have more helpful informations

# Custome your init() function

# isinstance(instance, Class)
# issubclass(Class1, Class2)

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

class Developer(Employee):
    def __init__(self, name, email, languages=None):
        super().__init__(name, email)
        #Employee(self, name, email)
        if languages is None:
            self.languages = []
        else:
            self.languages = languages

class Manager(Employee):
    def __init__(self, name, email, employees=None):
        super().__init__(name, email)
        #Employee(self, name, email)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)
    
    def remove_emp(self, emp):
        if emp not in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print('-->', emp.name)

# Print number of developer --> 2 --> Wrong ?
dev1 = Developer("TED", "TED.com", "Python")
dev2 = Developer("TED2", "TED2.com", "Shell")
emp1 = Employee("TED3", "TED3.com")
print(Employee.numb_of_emps)
print(Developer.numb_of_emps)

mgr_1 = Manager("Hoan", "Hoan.com")
mgr_1.add_emp(dev1)
mgr_1.add_emp(dev2)
mgr_1.add_emp(emp1)
mgr_1.print_emps()
mgr_1.remove_emp(dev2)
mgr_1.print_emps()
