'''An anagram of a string is another string that contains same characters, only the order of characters can be different.
For example, “abcd” and “dabc” are anagram of each other.'''
s1 = 'hello'
s2 = 'olhel'
if sorted(s1) == sorted(s2):
    print(s1, 'and', s2, "are anagram")