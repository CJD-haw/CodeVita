# 28. Write a Program to Find the sum of series: 1/1! + 1/2! + 1/3! + 1/4! + ... + 1/N!
"""
n = int(input("Enter the range of number : "))
sum = 0.0
fact = 1
for i in range(1, n+1):
    fact *= i
    sum += 1 / fact
print("The sum of the series =", sum)
"""

"""
from math import factorial
n = int(input())
result = [1 / factorial(val) for val in range(1, n+1)]
print(sum(result))
"""


def fact(num):
    f = 1
    for v in range(1, num+1):
        f *= v
    return f


print(sum([1 / fact(val) for val in range(1, int(input()) + 1)]))
