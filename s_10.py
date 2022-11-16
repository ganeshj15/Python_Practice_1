# python program to move the spaces from string to the front
s = 'both of these issues are fixed'
s_without_space = [i for i in s if i != ' ']
no_spaces = len(s) - len(s_without_space) # number of spaces
total_spaces = " " * no_spaces
rev_s = '"'+total_spaces + ''.join(s_without_space)+'"'
print("string after taking all spaces to the front:\n",rev_s)
