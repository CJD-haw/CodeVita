# 12. Write a Program to print series: 1 3 7 15 31 ... N
"""
n = int(input("Enter the range of number(Limit) : "))
i = 1
pr = 0
while i <= n:
    pr = (pr * 2) + 1
    print(pr, end=" ")
    i += 1
"""

n = int(input())
val = 1
for res in range(n):
    print(val, end=' ')
    val = (val * 2) + 1
