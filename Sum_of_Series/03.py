# 3. Write a Program to find the sum of series: 1^2 + 2^2 + 3^2 + ... + N^2
"""
print("Enter the range of number : ")
n = int(input())
sum = 0
for i in range(1, n+1):
    sum += i**2
print("The sum of the series =", sum)
"""

"""
n = int(input())
result = [val ** 2 for val in range(1, n+1)]
print(sum(result))
"""

print(sum([val ** 2 for val in range(1, int(input()) + 1)]))
