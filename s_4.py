# program to get the number of lower case characters in a string

s = 'DatA Science'
count = 0
for i in s:
    if i.islower():
        count += 1
print("number of lower case letter are:",count)