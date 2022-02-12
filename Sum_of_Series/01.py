# 1. Write a program to find the sum of series: 1 + 2 + 3 + ... + N
"""
print("Enter the range of number : ")
n = int(input())
sum = 0
for i in range(1, n+1):
    sum += i
print("The sum of the series =", sum)
"""

"""
n = int(input())
# result1 = n * (n + 1) // 2
# print(result1)
result2 = [val for val in range(1, n+1)]
print(sum(result2))
"""

print(sum([val for val in range(1, int(input()) + 1)]))
