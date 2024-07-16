# =============================================================================
'''
Create a function to test if a string is a valid pin or not.

A valid pin has:

Exactly 4 or 6 characters.
Only numerical characters (0-9).
No whitespace.
'''
# ===========================================================``
def Validate_Pin_check(pin):
    try:
        converted_pin=[]
        for x in str(pin):
            converted_pin.append(int(x))
            
        if len(converted_pin) == 4 or len(converted_pin)==6:
            for num in converted_pin:
                if int(num) >= 0 and int(num) <= 9:
                    return f'{pin} is vaild'
                else:
                  return  f'{pin} is invaild,please check and enter the pin again'
        return f'{pin} is invaild,please check and enter the pin again'
    except Exception as e :
        return f'check and enter pin again {e}'
    
result=Validate_Pin_check(12346)
print(result)
        
        
    