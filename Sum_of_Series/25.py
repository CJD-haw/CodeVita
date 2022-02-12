# 25. Write a Program to Find the sum of series: 1/2 + 2/3 + 3/4 + 4/5 + ... + N/(N+1)
"""
n = int(input("Enter the range of number : "))
sum = 0.0
for i in range(1, n+1):
    sum += i / (i + 1)
print("The sum of the series =", sum)
"""

"""
n = int(input())
result = [val / (val + 1) for val in range(1, n+1)]
print(sum(result))
"""

print(sum([val / (val + 1) for val in range(1, int(input()) + 1)]))
