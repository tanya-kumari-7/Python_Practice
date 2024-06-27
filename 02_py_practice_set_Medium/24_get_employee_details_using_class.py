# -*- coding: utf-8 -*-
"""
Created on Thu Jun 27 20:54:56 2024

@author: user
"""

# =============================================================================
# Create the instance attributes fullname and email in the Employee class.
# Given a person's first and last names:
# Form the fullname by simply joining the first and last name together,
# separated by a space.
# Form the email by joining the first and last name together with a .
# in between, and follow it with @company.com at the end. Make sure the 
# entire email is in lowercase.
# =============================================================================

class Employee:
    def __init__(self,first_name,last_name):
        self.first_name=first_name
        self.last_name=last_name
    
    def fullname(self):
        return f'{self.first_name.title()} {self.last_name.title()}'
    
    def email(self):
        return f'{self.first_name.lower()}.{self.last_name.lower()}@company.com'
    def firstname(self):
        return f'{self.first_name.title()}'
    
emp=Employee("John", "Smith")

print(emp.fullname())
print(emp.email())
print(emp.firstname())
        