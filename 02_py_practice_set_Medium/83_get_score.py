'''
4. Tuple Sorting
You are given a list of tuples where each tuple consists of a name and a score. Sort the list by score in descending order.

students = [('Alice', 80), ('Bob', 95), ('Charlie', 90)]
output = [('Bob', 95), ('Charlie', 90), ('Alice', 80)]

'''
students = [('Alice', 80), ('Bob', 95), ('Charlie', 90)]

def get_score(students):
    return students[1]

students_sorted = sorted(students,key= get_score,reverse= True)
print(students_sorted)


# def String_Processing_func(sentence):
#     check = 0
#     word = ''
#     for x in sentence.split():
#         if len(x) >= check:
#             word = x
#             check = len(x)
#         else:
#             continue
#     return word

# result = String_Processing_func(sentence)
# print(result)
            

