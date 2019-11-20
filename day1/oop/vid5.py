# Special methods: magic,  dunder

# Dunder init

# Dunder str
# def __repr__(self):
# Display more readable informations for end-users

# Dunder repr
# def __str__(self):
# Offen used for logging and debugging objects

# You can also custome more dunder methods to work with your objects:
# __add__()
# __len__()
# https://docs.python.org/3/reference/datamodel.html#special-method-names
# In realword, many libraries use this way to custome their method

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
    
    def __str__(self):
        return("Name: {0} | Email: {1}".format(self.name, self.email))

    def __repr__(self):
        return("Name: {0} | Email: {1}".format(self.name, self.email))

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

print(repr(dev1))