# 7. Write a Program to find the sum of series: 1 + X + X^2/2 + ...+ X^N/N
"""
print("Enter the range of number : ")
n = int(input())
print("Enter the value of x : ")
x = int(input())
sum = 1.0
i = 1
while i <= n:
    sum += pow(x, i) / i
    i += 1
print("The sum of the series =", sum)
"""

"""
n = int(input())
x = int(input())
result = [(x ** val) / val for val in range(1, n+1)]
print(1 + sum(result))
"""

N = int(input())
X = int(input())
print(sum([(X ** val) / val for val in range(1, N+1)]))
