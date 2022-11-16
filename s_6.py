#program to form new string made from first & last two characters from given string

s = 'software'
n = len(s)
rev_s = s[0:2]+s[n-2:]
print(rev_s)