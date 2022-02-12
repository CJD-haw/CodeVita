# 16. Write a Program to the find sum of series: 5^2 + 10^2 + 15^2 + ... + N^2
"""
import math
print("Enter the range of number(Limit) : ")
n = int(input())
i = 5
sum = 0
while i <= n:
    sum += pow(i, 2)
    i += 5
print("The sum of the series =", sum)
"""

"""
n = int(input())
result = [val ** 2 for val in range(5, n+1, 5)]
print(sum(result))
"""

print(sum([val ** 2 for val in range(5, int(input()) + 1, 5)]))

