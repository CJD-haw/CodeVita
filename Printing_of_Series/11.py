# 11. Write a Program to print series: 1 2 4 8 16 32 ... N
"""
n = int(input("Enter the range of number(Limit) : "))
i = 1
a = 1
while i <= n:
    print(a, end=" ")
    a *= 2
    i += 1
"""

n = int(input())
for val in range(n):
    print(2 ** val, end=' ')
