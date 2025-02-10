'''
Write a function that reverses a string. The input string is given as an array of characters s.

You must do this by modifying the input array in-place with O(1) extra memory.
'''

string = ["H","a","n","n","a","h"]

 
def Reverse_String_method1 (price):
    Reverse_String = list(reversed(string))
    return (Reverse_String)

Function_result1 = Reverse_String_method1(string)
print(Function_result1)

def Reverse_String_method2 (price):
    Reverse_String = price[::-1]
    return (Reverse_String)

Function_result2 = Reverse_String_method2(string)
print(Function_result2)

