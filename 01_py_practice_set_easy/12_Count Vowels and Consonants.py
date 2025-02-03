'''
Count Vowels and Consonants: Given a string, 
count the number of vowels and consonants.
'''
a = [1,2,3,4]

string = 'sonam'
def Vowels_Consonants_count_func(string):
    vowel =[]
    consonants = []
    for x in string:
        if x.lower() in 'aeiou': 
            vowel.append(x)
        else:
            consonants.append(x)
    return f" {len(vowel)} vowel & {len(consonants)} consonants in the string '{string}'"
            
result = Vowels_Consonants_count_func(string)
print(result)
