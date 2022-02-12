# 2. Write a Program to Print Square Number series 1 4 9 16 ...
"""
n = int(input("Enter the range of number(Limit) : "))
i = 1
while i <= n:
    print(i * i, end=" ")
    i += 1
"""

n = int(input())
for val in range(1, n+1):
    print(val ** 2, end=' ')
