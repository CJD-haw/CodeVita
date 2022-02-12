# 21. Write a program to find the sum of series: 1/2! + 2/3! + 3/4! + 4/5! + ... + N/(N+1)!
"""
n = int(input("Enter the range of number(Limit):"))
i = 1
sum = 0.0
while i <= n:
    sum += float(i / fact(i + 1))
    i += 1
print("The sum of the series =", sum)
"""

"""
from math import factorial
n = int(input())
result = [val / factorial(val+1) for val in range(1, n+1)]
print(sum(result))
"""


def fact(num):
    j = 1
    fa = 1
    while j <= num:
        fa *= j
        j += 1
    return fa


print(sum([val / fact(val+1) for val in range(1, int(input()) + 1)]))
