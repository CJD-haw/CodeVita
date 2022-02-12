# 7. Write a program to print series: 2 15 41 80 ... N
"""
print("Enter the range of number(Limit) : ")
n = int(input())
i = 1
value = 2
while i <= n:
    print(value, end=" ")
    value += i * 13
    i += 1
"""

n = int(input())
val = 2
for res in range(n):
    val += 13 * res
    print(val, end=' ')
