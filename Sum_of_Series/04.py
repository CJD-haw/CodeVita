
# 4. Write a Program to find the sum of series: 1^1 + 2^2 + 3^3 + ... + N^N
"""
import math
print("Enter the range of number : ")
n = int(input())
sum = 0
for i in range(1, n+1):
    sum += pow(i, i)
print("The sum of the series =", sum)
"""

"""
n = int(input())
result = [val ** val for val in range(1, n+1)]
print(sum(result))
"""

print(sum([val ** val for val in range(1, int(input()) + 1)]))


