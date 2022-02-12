# 6. Write a program to print series: -1 4 -7 10 -13 16 -19 ... N
"""
print("Enter the range of number(Limit) : ")
n = int(input())
i = 1
se = 1
while i <= n:
    if i % 2 == 0:
        print(se, end=" ")
    else:
        print(-1 * se, end=" ")
    se += 3
    i += 1
"""

n = int(input())
val = 1
for res in range(n):
    if val % 2 != 0:
        print(-val, end=' ')
    else:
        print(val, end=' ')
    val += 3
