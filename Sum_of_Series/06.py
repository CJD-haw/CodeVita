# 6. Write a Program to find the sum of series: X^1 + X^2 + X^3 + ... + X^N
"""
print("Enter the range of number : ")
n = int(input())
print("Enter the value of x : ")
x = int(input())
sum = 0
i = 1
while i <= n:
    sum += pow(x, i)
    i += 1
print("The sum of the series =", sum)
"""

"""
n = int(input())
x = int(input())
result = [x ** val for val in range(1, n+1)]
print(sum(result))
"""

N = int(input())
X = int(input())
print(sum([X ** val for val in range(1, N+1)]))
