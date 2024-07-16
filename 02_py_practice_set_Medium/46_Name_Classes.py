# -*- coding: utf-8 -*-
"""
Created on Mon Jul 15 19:47:21 2024

@author: user
"""

class Name:
    def __init__(self, first_name, last_name):
        self._first_name = first_name
        self._last_name = last_name
    
    def fullname(self):
        return f'{self._first_name.title()} {self._last_name.title()}'
    
    def get_first_name(self):
        return f'{self._first_name.title()}'
    
    def get_last_name(self):
        return f'{self._last_name.title()}'
    
    def initials(self):
        return f'{self._first_name[0].upper()}.{self._last_name[0].upper()}'
    
name_object = Name("john", "SMITH")
print(name_object.fullname())     # John Smith
print(name_object.get_first_name())   # John
print(name_object.get_last_name())    # Smith
print(name_object.initials())     # J.S
