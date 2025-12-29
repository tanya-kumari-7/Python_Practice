'''🔹 Question 1 
What is the difference between a list and a tuple in Python?
Explain with at least 3 points and one real use case.

Lists and tuples are both ordered collections that can store heterogeneous data types.
    The main difference is that lists are mutable, meaning elements can be added, removed, or modified, whereas tuples are immutable once created.
    Because tuples are immutable, they are more memory-efficient and faster than lists and can be used as dictionary keys, which lists cannot.
Use case:
Use a tuple when data should remain constant, e.g., configuration settings or historical records.
Use a list when data is expected to change, e.g., a list of students where new admissions can happen.



Question 2
What is the difference between:
a = [1, 2, 3]
b = a
c = a.copy()

What happens if we do a.append(4)?
What will be the values of a, b, and c?
Why?
    a.append(4) : Modifies the original list in place
    b = a → reference copy (same memory)
    c = a.copy() → shallow copy (new memory)
'''