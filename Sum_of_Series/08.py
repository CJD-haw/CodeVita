# 8. Write a Program to find the sum of series: 1 + X + X^2/2! + X^3/3! + ... + X^N/N!
"""
print("Enter the range of number : ")
n = int(input())
print("Enter the value of x : ")
x = int(input())
sum = 1.0
i = 1
while i <= n:
    fact = 1
    for j in range(1, i+1):
        fact *= j
    sum += pow(x, i) / fact
    i += 1
print("The sum of the series = ",sum)
"""


def fact(num):
    f = 1
    for v in range(1, num+1):
        f *= v
    return f


""" 
n = int(input())
x = int(input())
result = [(x ** val) / fact(val) for val in range(1, n+1)]
print(1 + sum(result))
"""

N = int(input())
X = int(input())
print(1 + sum([(X ** val) / fact(val) for val in range(1, N+1)]))
