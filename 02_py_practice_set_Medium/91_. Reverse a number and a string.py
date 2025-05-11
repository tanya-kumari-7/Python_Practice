del str


name = 'sonam'
num = 123458976

# Function to reverse a string
def reverse_string(s):
    return s[::-1]

result = reverse_string(name)
print("Reversed name:", result)

# Function to reverse a number
def reverse_number(n):
    return str(n)[::-1]  # Convert to string and reverse it

num_reversed = reverse_number(num)
print("Reversed number (as string):", num_reversed)

# Function to reverse a number using loop


############ Method 1 

num = 123467744
for x in str(num):
    print(str(num)[::-1])
    break

############# method 2 
