# 9. Write a program to print series: 0 6 10 17 22 30 36 ... N
"""
print("Enter the range of number(Limit) : ")
n = int(input())
i = 1
a = 0
b = 6
k = 10
p = 11
while i <= n:
    if i % 2 == 0:
        print(b, end=" ")
        b += p
        p += 2
    else:
        print(a, end=" ")
        a += k
        k += 2
    i += 1
"""

n = 7
a, b, c, x, y = 0, 6, 2, 10, 11
for res in range(1, n+1):
    if res % 2 != 0:
        print(a, end=' ')
        a += x
        x += c
    else:
        print(b, end=' ')
        b += y
        y += c
