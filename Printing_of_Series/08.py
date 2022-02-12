# 8. Write a program to print series: 10 5 60 15 110 ... N
"""
print("Enter the range of number(Limit) : ")
n = int(input())
a = 10
b = 5
i = 1
while i <= n:
    if i%2 == 0:
        print(b, end=" ")
        b += 10
    else:
        print(a, end=" ")
        a += 50
    i += 1
"""

n = int(input())
a, b = 10, 5
for val in range(1, n+1):
    if val % 2 != 0:
        print(a, end=' ')
        a += 50
    else:
        print(b, end=' ')
        b += 10
