
"""
The Fibonacci numbers are the numbers in the following integer sequence 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
In mathematical terms, the sequence Fn of Fibonacci numbers is defined by the recurrence relation
Fn = Fn-1 + Fn-2
"""

n = int(input())
if n < 2:
    print('Invalid Input')
    exit()

a = 0
b = 1
result = [0, 1]
for i in range(1, n):
    c = a + b
    a = b
    b = c
    result.append(c)

# print(result)
for val in result:
    print(val, end=', ')

