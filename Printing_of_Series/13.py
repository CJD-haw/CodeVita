# 13. Write a Program to print series: 1 -2 6 -15 31 ... N
"""
n = int(input("Enter the range of number(Limit) : "))
i = 1
pr = 1
while i <= n:
    if i % 2 == 0:
        print(-1 * pr, end=" ")
    else:
        print(pr, end=" ")
    pr += pow(i, 2)
    i += 1
"""

n = int(input())
val = 1
for res in range(1, n+1):
    if res % 2 != 0:
        print(val, end=' ')
    else:
        print(-val, end=' ')
    val += res ** 2
