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
    
    def fullname(self,first_name,last_name):
        return f'{first_name.title()} {last_name.title()}'
    
    def email(self,first_name,last_name):
        return f'{first_name.lower()}.{last_name.lower()}@company.com'
    def firstname(self,first_name,last_name):
        return f'{first_name.title()}'
    
emp=Employee()

print(emp.fullname("John", "Smith"))
print(emp.email("John", "Smith"))
print(emp.firstname("John", "Smith"))
        