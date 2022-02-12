# 18. Write a Program to print series: 0 2 6 12 20 30 42 ... N
"""
n = int(input("Enter the range of number(Limit) : "))
i = 1
while i <= n:
    print((i * i) - i, end=" ")     # n(n-1) formula
    i += 1
"""

n = int(input())
val = 0
offset = 2
for res in range(n):
    print(val, end=' ')
    val += offset
    offset += 2
