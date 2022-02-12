# 20. Write a Program to find the sum of series: 1 + 4 + 9 + 16 + 25 + ... + N
"""
import math
print("Enter the range of number(Limit) : ")
n = int(input())
i = 1
sum = 0.0
while i <= n:
    sum += pow(i, 2)
    i += 1
print("The sum of the series =", sum)
"""

"""
n = int(input())
result = [(val ** 2) for val in range(1, n+1)]
print(sum(result))
"""

print(sum([val ** 2 for val in range(1, int(input()) + 1)]))
