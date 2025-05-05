# Write a function to return all chars which are present consecutively twice in a string

name = 'commit'

check = []
for x in range(len(name)-1):
   if name[x] == name[x+1]:
         check.append(name[x])
   else:
       continue

print(check)

    