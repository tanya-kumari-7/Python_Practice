'''
What is the difference between:
list
tuple
set
dictionary
Also mention one use case for each.

####################################################

List: Ordered, mutable collection → [1, 2, 3]
👉 Use case: When you need to modify data (e.g., storing user transactions)

Tuple: Ordered, immutable collection → (1, 2, 3)
👉 Use case: Fixed data (e.g., coordinates, config values)

Set: Unordered, no duplicates → {1, 2, 3}
👉 Use case: Removing duplicates or membership checks

Dictionary: Key-value pairs → {"name": "Tanya", "age": 25}
👉 Use case: Mapping data (e.g., user_id → user_details)

#####################################################
'''

'''
What is the difference between:

deep copy
shallow copy
And give a small example where shallow copy can cause issues.

#####################################################
Shallow Copy

Copies only the outer object
Inner objects (nested) still share the same memory reference
👉 So changes inside nested structures affect both

Example:
import copy

a = [[1, 2], [3, 4]]
b = copy.copy(a)

b[0][0] = 100
print(a)  # [[100, 2], [3, 4]]  ← changed!

Deep Copy
Copies everything recursively
Completely independent memory

👉 Changes do NOT affect original

Example:
import copy
a = [[1, 2], [3, 4]]
b = copy.deepcopy(a)

b[0][0] = 100
print(a)  # [[1, 2], [3, 4]]  ← unchanged

#####################################################
'''

'''

#####################################################

#####################################################
'''

###########