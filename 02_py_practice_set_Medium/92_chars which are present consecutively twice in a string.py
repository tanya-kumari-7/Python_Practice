# Write a function to return all chars which are present consecutively twice in a string

name = 'commit'

check = []
for x in range(len(name)-1):
   if name[x] == name[x+1]:
         check.append(name[x])
   else:
       continue

print(check)

# create a function to return two sub strings one with chars available at even index and other available at odd index.

name = 'sonam'
odd = ""
even = ""
for index , text in enumerate(name):
   # print(index,text)
   if index % 2 == 0:
       even += text
   else:
       odd += text
       
print(f"odd char in string [{name}] is {odd} \nEven char in string [{name}] is {even}")
    