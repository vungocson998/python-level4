# Property decorators: define functions but we can access it like an attribute
# @property
# def function(self):
#     pass

# You want some functions or attributes update automatically whenever you change some attributes in yours instances
# For example when you change name of some employees, their emails will be changed automatically 

# Setter:
# @name_property.setter
# def function(self, new_value):
#      self.attr1 = v1
#      self.attr2 = v2
# Examples: instance.function = new_value

# Deleter:
# @name_property.deleter
# def function(self):
#      self.attr1 = None
#      self.attr2 = None
# Examples: del instance.function

class Employee:
    numb_of_emps = 0
    company = "Home"
    def __init__(self, name):
        self.name = name
        Employee.numb_of_emps += 1

    @property    
    def email(self):
        return "{0}@gmail.com.vn".format(self.name)

emp1 = Employee("TED") 

print(emp1.email)