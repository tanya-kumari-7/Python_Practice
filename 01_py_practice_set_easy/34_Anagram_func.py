      
"""
📌 7️⃣ Anagram Checker
Check if two strings are anagrams:

Input: "listen", "silent" → True
"""      
  
string = 'listen'
string2 = 'Silent'

def Anagram_func(value,value2):
    if sorted(value.lower()) == sorted(value2.lower()):
        return f'Yes it is a Anagram'
    else:
        return f'No, it is not a Anagram'
   

result2 = Anagram_func(string,string2)
print(result2)
