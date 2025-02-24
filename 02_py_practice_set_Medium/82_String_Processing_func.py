'''
3. String Processing
Write a function that takes a sentence as input and returns the longest word in the sentence. If there are multiple words of the same maximum length, return the first one.

Example:

sentence = "Python is an amazing programming language"
output = "programming"

'''
sentence = "Python is an amazing programming language"

def String_Processing_func(sentence):
    check = 0
    word = ''
    for x in sentence.split():
        if len(x) >= check:
            word = x
            check = len(x)
        else:
            continue
    return word

result = String_Processing_func(sentence)
print(result)
            

