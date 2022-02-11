
"""
Given a string, write a python function to check if it is palindrome or not.
A string is said to be palindrome if the reverse of the string is the same as string.
For example, “radar” is a palindrome, but “radix” is not a palindrome.
"""

s = 'radix'
r = ''
for v in s:
    r = v + r
    if r == s:
        print('Yes')
        exit()
else:
    print('No')
