# 20. Write a Program to print series: 1 9 17 33 49 73 97 ... N
"""
n = int(input("Enter the range of number(Limit) : "))
i = 1
pr = 0
while i <= n:
    if i % 2 == 0:
        pr = 2 * pow(i, 2) + 1
        print(pr, end=" ")
    else:
        pr = 2 * pow(i, 2) - 1
        print(pr, end=" ")
    i += 1
"""

n = int(input())
for odd, even in zip(range(1, n+1, 2), range(2, n+1, 2)):
    print(2 * (odd ** 2) - 1, 2 * (even ** 2) + 1, end=' ')
if n % 2 != 0:
    print(2 * (n ** 2) - 1)
