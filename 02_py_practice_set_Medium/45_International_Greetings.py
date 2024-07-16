# -*- coding: utf-8 -*-
"""
Created on Mon Jul 15 19:47:21 2024

@author: user
"""
# =============================================================================
'''
Suppose you have a guest list of students and the country 
they are from, stored as key-value pairs in a dictionary.

GUEST_LIST = {
"Randy": "Germany",
"Karla": "France",
"Wendy": "Japan",
"Norman": "England",
"Sam": "Argentina"
}
Write a function that takes in a name and returns a name tag,
that should read:

"Hi! I'm [name], and I'm from [country]."
If the name is not in the dictionary, return:
"Hi! I'm a guest."
'''
# =============================================================================

def International_Greetings(name):
    guest_list = {
    "Randy": "Germany",
    "Karla": "France",
    "Wendy": "Japan",
    "Norman": "England",
    "Sam": "Argentina"
    }
    for guest_list_name,country in guest_list.items():
        if name.lower() == guest_list_name.lower():
            return f"Hi! I'm {guest_list_name}, and I'm from {country}"
    return f"Hi! I'm a guest"
    
result=International_Greetings('monti')
print(result)
        
    
