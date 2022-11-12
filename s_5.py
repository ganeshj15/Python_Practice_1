#program to take hyphen separated words and print the words in hyphen separated sequence after sorting them.

s = 'python-is-easy-to-understand'
words = s.split("-")
new_words= sorted(words) # by-default its sorts the alphabetically
print("sorted string is:","-".join(new_words))
#print('-'.join(sorted(words)))