# 10. Write a program to print series: 6 9 14 21 30 41 54 ... N
"""
print("Enter the range of number(Limit) : ")
n = int(input())
i = 1
j = 3
value = 6
while i <= n:
    print(value, end=" ")
    value += j
    j += 2
    i += 1
"""

n = 7
val = 6
offset = 3
for res in range(n):
    print(val, end=' ')
    val += offset
    offset += 2
