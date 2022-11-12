# Program to get the number of vowels in a string

def get_vowels(s):
    vowels = 'aeiou'
    count = 0
    for i in s:
        if i in vowels:
            count += 1
    return count


s = get_vowels('python is high level language')
print("number of vowels are :", s)