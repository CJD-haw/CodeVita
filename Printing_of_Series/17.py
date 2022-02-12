# 17. Write a Program to print series: 1 2 5 8 15 28 51 94 ... N
"""
n = int(input("Enter the range of number(Limit) : "))
i = 4
if n >= 1:
    print("1", end=" ")
if n >= 2:
    print("2", end=" ")
if n >= 3:
    print("5", end=" ")
a = 1
b = 2
c = 5
while i <= n:
    d = a + b + c
    a = b
    b = c
    c = d
    print(d, end=" ")
    i += 1
"""

n = int(input())
a, b, c, d = 1, 2, 5, 0
for res in range(1, n+1):
    if res == 1:
        print(a, end=' ')
    elif res == 2:
        print(b, end=' ')
    elif res == 3:
        print(c, end=' ')
    else:
        d = a + b + c
        a, b, c = b, c, d
        print(d, end=' ')
