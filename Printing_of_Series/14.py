# 14. Write a Program to print series: 6 11 21 36 56 ...N
"""
n = int(input("Enter the range of number(Limit) : "))
i = 1
pr = 6
diff = 5
while i <= n:
    print(pr, end=" ")
    pr = pr + diff
    diff = diff + 5
    i += 1
"""

n = int(input())
a, b = 6, 5
for res in range(n):
    print(a, end=' ')
    a += b
    b += 5
