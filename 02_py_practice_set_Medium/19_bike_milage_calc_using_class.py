# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 22:02:42 2024

@author: user
"""

class bike:
    
    def __init__(self,load):
        self.load=load
        
    def milage(self,km):
        mlg=self.load*km
        return f"milage is {mlg}"
    
    def torque(self,mass):
        tor=self.load*mass
        return f"torque is {tor}"
    
Activa_object= bike(70)
print(Activa_object.milage(10))
print(Activa_object.torque(80))

ntorq_object=bike(100)
print(ntorq_object.milage(100))
print(ntorq_object.torque(200))
        
    