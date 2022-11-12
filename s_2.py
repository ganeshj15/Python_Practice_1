# programme to get the new string where first & last characters of original string are exchanged.

s = 'git hub'
new_s = s[-1] + s[1:-1] +s[0]
print("original string:",s)
print("String after exchanging:",new_s)