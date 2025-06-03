string_input = "soonamjklmn"

bucket = ""         # Current substring without repeats
check = []          # List to keep track of characters in current substring
max_len = 0         # Track max length found so far
max_substr = ""     # Track longest substring

for x in string_input:
    if x not in check:
        bucket += x
        check.append(x)
        if len(bucket) > max_len:
            max_len = len(bucket)
            max_substr = bucket
    else:
        # If character is repeated:
        # Find where it occurred before
        dup_index = check.index(x)
        
        # Remove characters from start to duplicate
        check = check[dup_index + 1:]
        bucket = bucket[dup_index + 1:]
        
        # Add current character
        check.append(x)
        bucket += x

print("Length of longest substring:", max_len)
print("Longest substring:", max_substr)

