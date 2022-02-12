# 16. Write a Program to print series: 0 2 8 14 24 34 ... N
"""
n = int(input("Enter the range of number(Limit) : "))
i = 1
pr = 0
while i <= n:
    if i%2 == 0:
        pr=pow(i, 2) - 2
        print(pr, end=" ")
    else:
        pr = pow(i, 2) - 1
        print(pr, end=" ")
    i += 1
"""

n = int(input())
for odd, even in zip(range(1, n+1, 2), range(2, n+1, 2)):
    print(odd**2 - 1, even**2 - 2, end=' ')
if n % 2 != 0:
    print(n**2 - 1)
