'''
6.File Handling
Write a Python program that reads a file called data.txt, counts the number of words in it, and prints the count.

'''

def count_words_in_file(filename):
    try:
        with open(filename,'r',encoding='utf-8') as file:
            content = file.read()
            words = content.split()
            return len(words)
    except FileNotFoundError:
        return 'Error: File not Found!'
    except Exception as e:
        return 'Error: File not Found!'
        

filename = "C:/Users/user/Downloads/data.txt"
result = count_words_in_file(filename)
print(result)
            

