
"""
Problem Statement:
    Find the 15th term of the series 0, 0, 7, 6, 14, 12, 21, 18, 28, 24

Explanation:
    In this series the odd term is increment of 7 {0, 7, 14, 21, 28, 35 – – – – – – }
    And even term is a increment of 6 {0, 6, 12, 18, 24, 30 – – – – – – }
"""

"""
num = int(input('enter the number: '))
a=0
b=0
for i in range(1, num+1):
    if(i % 2 != 0):
        a = a + 7
    else:
        b = b + 6

if(num % 2 != 0):
    print('{} term of series is {}'.format(num, a-7))
else:
    print('{} term of series is {}'.format(num, b-6))
"""

e, o = 0, 0
n = 15
s = []

for i in range(1, n+1):
    if i % 2 == 0:
        s.append(e)
        e += 6
    else:
        s.append(o)
        o += 7
    print(s[-1], end=', ')

print('\n{0}th term of the series is {1}'.format(n, s[-1]))
