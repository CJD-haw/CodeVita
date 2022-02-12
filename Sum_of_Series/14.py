# 14. Write a program to find the sum of series: 1^1/1! + 2^2/2! + 3^3/3! + ... + N^N/N!
"""
import math
print("Enter the range of number : ")
n = int(input())
sum = 0.0
fact = 1
for i in range(1, n+1):
    fact *= i
    sum += pow(i, i) / fact
print("The sum of the series =", sum)
"""

"""
from math import factorial
n = int(input())
result = [(val ** val) / factorial(val) for val in range(1, n+1)]
print(sum(result))
"""


def fact(num):
    f = 1
    for v in range(1, num+1):
        f *= v
    return f


print(sum([(val ** val) / fact(val) for val in range(1, int(input()) + 1)]))


