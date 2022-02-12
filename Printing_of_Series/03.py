# 3. Write a Program to print Cube Number series 1 8 27 64 ...
"""
print("Enter the range of number(Limit) : ")
n = int(input())
i = 1
while i <= n:
    print(i * i * i, end=" ")
    i += 1
"""

n = int(input())
for val in range(1, n+1):
    print(val ** 3, end=' ')
