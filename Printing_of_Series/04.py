# 4. Write a Program to print Triangular Number series 1 3 6 10 15 ...
"""
print("Enter the range of number(Limit) : ")
n = int(input())
i = 1
while i <= n:
    print(int((i * (i + 1)) / 2), end=" ")
    i += 1
"""

n = int(input())
for val in range(1, n+1):
    new = val + 1
    print(int(val * new / 2), end=' ')
