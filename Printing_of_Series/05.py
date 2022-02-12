# 5. Write a Program to print the Fibonacci series.
"""
print("Enter the range of number(Limit) : ")
n = int(input())
i = 1
a = 0
b = 1
c = a + b
while i <= n:
    print(c, end=" ")
    c = a + b
    a = b
    b = c
    i += 1
"""

n = int(input())
a, b, c = 0, 1, 0
if n >= 2:
    # print(a, end=' ')
    for res in range(n):
        a = b
        b = c
        c = a + b
        print(c, end=' ')
else:
    print('Invalid Input')
